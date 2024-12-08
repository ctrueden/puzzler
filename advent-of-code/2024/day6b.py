with open("day6.txt") as f:
    lines = [line.strip() for line in f.readlines()]

h = len(lines)
w = len(lines[0])

directions = {
    "^": (+0, -1), # up
    ">": (+1, +0), # right
    "v": (+0, +1), # down
    "<": (-1, +0), # left
}
turns = {
    (+0, -1): (+1, +0), # ^ to >
    (+1, +0): (+0, +1), # > to v
    (+0, +1): (-1, +0), # v to <
    (-1, +0): (+0, -1), # < to ^
}


def tick(board, px, py, dx, dy):
    nx, ny = px + dx, py + dy
    if (
        nx >= 0 and nx < w and
        ny >= 0 and ny < h and
        board[py + dy][px + dx] == "#"
    ):
        # Obstacle! Turn right.
        return (px, py) + turns[(dx, dy)]

    # No obstacle. Advance in this direction.
    return nx, ny, dx, dy


# Find initial guard position and direction.
px, py, dx, dy = None, None, None, None
for y in range(h):
    for x in range(w):
        c = lines[y][x]
        if c in directions:
            assert px is None
            px, py = x, y
            dx, dy = directions[c]
assert px is not None


def loops(board, px, py, dx, dy):
    visited = set()
    while True:
        if (px, py, dx, dy) in visited:
            # Caught in a loop!
            return True
        visited.add((px, py, dx, dy))
        px, py, dx, dy = tick(board, px, py, dx, dy)
        if px < 0 or px >= w or py < 0 or py >= h:
            # Guard has left the scene!
            return False


total = 0
for y in range(h):
    for x in range(w):
        if lines[y][x] == ".":
            # Try replacing this empty square with an obstacle.
            board = lines.copy()
            board[y] = board[y][0:x] + "#" + board[y][x+1:]
            if loops(board, px, py, dx, dy):
                print(x, y)
                total += 1

print(total)
