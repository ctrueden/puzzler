from collections import deque
from typing import List, Tuple, Optional
import sys
import random


def ball_sort(tubes: int, capacity: int, balls: List[str]) -> List[Tuple[int, int]]:
    """
    Solve the ball sorting problem using BFS.

    Args:
        tubes: Number of tubes
        capacity: Maximum capacity per tube
        balls: Initial state - list of strings representing ball colors in each tube

    Returns:
        List of (from_tube, to_tube) moves to solve the puzzle
    """
    # Convert input to list of lists for easier manipulation
    tubes = [list(tube) for tube in balls]

    def is_solved(state):
        """Check if the puzzle is solved."""
        empty_count = 0
        for tube in state:
            if not tube:  # Empty tube
                empty_count += 1
                continue
            # Non-empty tube must have exactly (capacity-1) balls of same color
            if len(tube) != capacity - 1 or len(set(tube)) != 1:
                return False
        # Must have exactly one empty tube
        return empty_count == 1

    def get_valid_moves(state):
        """Get all valid moves from current state."""
        moves = []
        for from_idx in range(len(state)):
            if not state[from_idx]:  # Can't move from empty tube
                continue

            ball_to_move = state[from_idx][-1]  # Top ball

            for to_idx in range(len(state)):
                if from_idx == to_idx:  # Can't move to same tube
                    continue
                if len(state[to_idx]) >= capacity:  # Target tube is full
                    continue
                if state[to_idx] and state[to_idx][-1] != ball_to_move:  # Can only stack same colors
                    continue

                moves.append((from_idx, to_idx))

        return moves

    def make_move(state, from_idx, to_idx):
        """Create new state after making a move."""
        new_state = [tube[:] for tube in state]  # Deep copy
        ball = new_state[from_idx].pop()
        new_state[to_idx].append(ball)
        return new_state

    def state_to_tuple(state):
        """Convert state to hashable tuple for visited set."""
        return tuple(tuple(tube) for tube in state)

    # BFS to find shortest solution
    queue = deque([(tubes, [])])  # (state, moves)
    visited = {state_to_tuple(tubes)}

    while queue:
        current_state, moves = queue.popleft()

        if is_solved(current_state):
            return moves

        for from_idx, to_idx in get_valid_moves(current_state):
            new_state = make_move(current_state, from_idx, to_idx)
            state_key = state_to_tuple(new_state)

            if state_key not in visited:
                visited.add(state_key)
                new_moves = moves + [(from_idx, to_idx)]
                queue.append((new_state, new_moves))

    return []  # No solution found


def print_solution(tubes: int, capacity: int, balls: List[str], moves: List[Tuple[int, int]]):
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


def generate_random_puzzle(tubes: int, capacity: int) -> List[str]:
    """Generate a random starting configuration for the ball sort puzzle."""
    colors = "abcdefghijklmnopqrstuvwxyz"[:tubes-1]  # Use first n-1 letters as colors

    # Create all balls: (capacity-1) balls of each color
    all_balls = []
    for color in colors:
        all_balls.extend([color] * (capacity - 1))

    # Shuffle the balls
    random.shuffle(all_balls)

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
    if len(sys.argv) >= 3:
        test_tubes = int(sys.argv[1])
        test_capacity = int(sys.argv[2])
    else:
        print("Usage: python ball_sort.py <tubes> <capacity>")
        print("Using default values: 4 tubes, capacity 3")
        test_tubes = 4
        test_capacity = 3

    # Generate random starting configuration
    test_balls = generate_random_puzzle(test_tubes, test_capacity)

    print(f"Solving ball sort puzzle with {test_tubes} tubes, max capacity {test_capacity}")
    print(f"Initial configuration: {test_balls}")
    print()

    moves = ball_sort(test_tubes, test_capacity, test_balls)

    if moves:
        print(f"Solution found in {len(moves)} moves!")
        print_solution(test_tubes, test_capacity, test_balls, moves)
    else:
        print("No solution found!")
