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

positions = set()
while True:
    positions.add((px, py))
    px, py, dx, dy = tick(lines, px, py, dx, dy)
    if px < 0 or px >= w or py < 0 or py >= h:
        # Guard has left the scene!
        break

print(len(positions))
