from multiprocessing import Pool
from queue import PriorityQueue
import random
import sys
import time


class BallState:
    def __init__(self, tubes: list[list[str]], capacity: int, moves_taken: int = 0):
        self.tubes: list[list[str]] = tubes
        self.capacity = capacity
        self.moves_taken = moves_taken

    def __lt__(self, other):
        return self.score() < other.score()

    def __hash__(self):
        # Note: This does not include moves_taken.
        # For "equality" that is technically incorrect...
        # But for the visited set, it's what we need.

        # Convert tubes to hashable tuple for visited set.
        tubes_tuple = tuple(tuple(tube) for tube in self.tubes)
        return hash((tubes_tuple, self.capacity))

    def __eq__(self, other):
        # Note: This does not include moves_taken.
        # For "equality" that is technically incorrect...
        # But for the visited set, it's what we need.
        return self.tubes == other.tubes and self.capacity == other.capacity

    def how_many_moves_left(self) -> int:
        misses = 0
        # TODO: We want to improve the cost function.
        #
        # Curtis's half-baked idea:
        # - Decide what color each tube "should" be, based on the most represented color in the tube
        #
        # Eric's maybe good idea:
        # - It takes X moves to remove the top X balls of wrong color.
        # - Then it takes at least Y moves to add Y balls of the needed color.
        # - So the misses is X + Y.
        # - But a "Y" removal in one tube could also be an "X" move in another tube.
        #   - So we should divide by 2 to avoid overestimating.
        for tube in self.tubes:
            # BBBRB-  ==>  2 misses, not 1
            if len(tube) == 0:
                # Tube is empty; score is capacity - 1
                pass  # misses += 0 -- there is one empty tube
            else:
                correct_ball = tube[0]

                # Find the index of the first ball that is not the correct ball.
                # BBBB--  ==> first "wrong" index is 4 -- counts as 6-4-1 = 1 miss
                first_wrong_index = len(tube)
                for i, ball in enumerate(tube):
                    if ball != correct_ball:
                        first_wrong_index = i
                        break
                misses += self.capacity - first_wrong_index - 1

        return misses

    def score(self) -> int:
        return self.moves_taken + self.how_many_moves_left()

    def make_move(self, from_idx, to_idx) -> "BallState":
        """Create new state after making a move."""
        tubes = [tube[:] for tube in self.tubes]  # Deep copy
        ball = tubes[from_idx].pop()
        tubes[to_idx].append(ball)
        return BallState(tubes, self.capacity, self.moves_taken + 1)

    def is_solved(self):
        """Check if the puzzle is solved."""
        empty_count = 0
        for tube in self.tubes:
            if not tube:  # Empty tube
                empty_count += 1
                continue
            # Non-empty tube must have exactly (capacity-1) balls of same color
            if len(tube) != self.capacity - 1 or len(set(tube)) != 1:
                return False
        # Must have exactly one empty tube
        return empty_count == 1

    def get_valid_moves(self):
        """Get all valid moves from current state."""
        moves = []
        for from_idx in range(len(self.tubes)):
            if not self.tubes[from_idx]:  # Can't move from empty tube
                continue

            ball_to_move = self.tubes[from_idx][-1]  # Top ball

            for to_idx in range(len(self.tubes)):
                if from_idx == to_idx:  # Can't move to same tube
                    continue
                if len(self.tubes[to_idx]) >= self.capacity:  # Target tube is full
                    continue
                if self.tubes[to_idx] and self.tubes[to_idx][-1] != ball_to_move:  # Can only stack same colors
                    continue

                moves.append((from_idx, to_idx))

        return moves


def ball_sort_dumb(capacity: int, balls: list[str]) -> int | None:
    """
    Solve the ball sorting problem using A*.

    Args:
        capacity: Maximum capacity per tube
        balls: Initial state - list of strings representing ball colors in each tube

    Returns:
        List of (from_tube, to_tube) moves to solve the puzzle
    """
    # Convert input to list of lists for easier manipulation
    tubes = [list(tube) for tube in balls]
    state = BallState(tubes, capacity)
    return ball_sort(state)


def ball_sort(state: BallState) -> int | None:

    # BFS to find shortest solution
    queue = PriorityQueue()
    queue.put((0, (state, [])))  # (state, moves)
    visited = {state}

    count = 0
    # Every move: O(N^2) possibilities - "Branching factor"
    # How many moves? "exponential"...
    
    # Heuristic:
    # - Assume bottom/first ball is "correct"
    # - everything non-matching above is "incorrect"
    while queue:
        score, item = queue.get()
        current_state, moves = item
        count += 1

        if current_state.is_solved():
            print(f"SUCCESS count: {count}")
            return len(moves)

        for from_idx, to_idx in current_state.get_valid_moves():
            new_state: BallState = current_state.make_move(from_idx, to_idx)

            if new_state not in visited:
                visited.add(new_state)
                new_moves = moves + [(from_idx, to_idx)]
                queue.put((new_state.score(), (new_state, new_moves)))

    print(f"FAILURE count: {count}")
    return None  # No solution found


def print_solution(tubes: int, capacity: int, balls: list[str], moves: list[tuple[int, int]]):
    """Print the step-by-step solution."""
    tubes = [list(tube) for tube in balls]

    print("Initial state:")
    for i, tube in enumerate(tubes):
        print(f"Tube {i}: {''.join(tube) if tube else 'empty'}")
    print()

    for step, (from_idx, to_idx) in enumerate(moves, 1):
        ball = tubes[from_idx].pop()
        tubes[to_idx].append(ball)

        print(f"Step {step}: Move '{ball}' from tube {from_idx} to tube {to_idx}")
        for i, tube in enumerate(tubes):
            print(f"Tube {i}: {''.join(tube) if tube else 'empty'}")
        print()


def generate_random_puzzle(seed: int, tubes: int, capacity: int) -> list[str]:
    """Generate a random starting configuration for the ball sort puzzle."""
    colors = "abcdefghijklmnopqrstuvwxyz"[:tubes-1]  # Use first n-1 letters as colors

    # Create all balls: (capacity-1) balls of each color
    all_balls = []
    for color in colors:
        all_balls.extend([color] * (capacity - 1))

    # Shuffle the balls
    r = random.Random(seed)
    r.shuffle(all_balls)

    # Distribute balls into tubes (all but the last tube get capacity-1 balls)
    balls = []
    ball_idx = 0
    for tube_idx in range(tubes - 1):
        tube_balls = all_balls[ball_idx:ball_idx + capacity - 1]
        balls.append(''.join(tube_balls))
        ball_idx += capacity - 1

    # Last tube starts empty
    balls.append("")

    return balls


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) >= 4:
        seed = int(sys.argv[1])
        test_tubes = int(sys.argv[2])
        test_capacity = int(sys.argv[3])
    elif len(sys.argv) == 3:
        seed = int(sys.argv[1])
        test_tubes = int(sys.argv[2])
        test_capacity = test_tubes - 1
    else:
        print("Usage: python ball_sort.py <seed> <tubes> <capacity>")
        print("Using default values: 12345 seed, 4 tubes, capacity 3")
        seed = 12345
        test_tubes = 4
        test_capacity = 3

    # Generate random starting configuration
    test_balls = generate_random_puzzle(seed, test_tubes, test_capacity)
    #test_balls = ['bc', 'ca', 'ba', '']

    print(f"Solving ball sort puzzle with {test_tubes} tubes, max capacity {test_capacity}")
    print(f"Initial configuration: {test_balls}")
    print()

    def print_time(t1, t2):
        print(f"TIME: {(t2 - t1) / 1_000_000_000} seconds")

    # Solve single threaded.
    time1 = time.time_ns()
    dumb_moves = ball_sort_dumb(test_capacity, test_balls)
    time2 = time.time_ns()
    print(f"Slow algorithm in {dumb_moves} moves")
    print_time(time1, time2)

    # Now solve with multiprocessing.

    time3 = time.time_ns()

    initial_state = BallState([list(tube) for tube in test_balls], test_capacity)
    if initial_state.is_solved():
        print("WHAT ARE YOU DOING? NOTHING.")

    neighbors = []
    for from_idx, to_idx in initial_state.get_valid_moves():
        new_state: BallState = initial_state.make_move(from_idx, to_idx)
        neighbors.append(new_state)

    with Pool(16) as p:
        result = [v for v in p.map(ball_sort, neighbors) if v is not None]
        moves = 1 + min(result)

    time4 = time.time_ns()

    if moves:
        print(f"Solution found in {moves} moves!")
        #print_solution(test_tubes, test_capacity, test_balls, moves)
    else:
        print("No solution found!")

    print_time(time3, time4)

    print("DONE")
