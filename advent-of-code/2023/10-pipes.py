# Simple:
# .....
# .012.
# .1.3.
# .234.
# .....


# Slightly more complex:
# ..45.
# .236.
# 01.78
# 14567
# 23...

infile = "10-input.txt"

with open(infile) as f:
    lines = [line.strip() for line in f.readlines()]

Pos = tuple[int, int]
Step = tuple[int, int]

class Field:
    def __init__(self, lines):
        self.lines = lines
        self.rowCount = len(lines)
        self.colCount = len(lines[0]) # NB: Assumes same-length lines.

    def start(self) -> Pos:
        for i, line in enumerate(self.lines):
            s = line.find("S")
            if s >= 0: return i, s
        raise RuntimeError("THERE IS NO START WTF")

    def square(self, row, col):
        return (
            '.'
            if row < 0 or row >= self.rowCount or col < 0 or col >= self.colCount
            else
            lines[row][col]
        )

field = Field(lines)

print("Input:")
for line in lines: print(line)
print()
print(f"Start: {field.start()}")

# NB: Coordinates are (y, x) -- i.e. (vertical, horizontal) -- i.e. (row, col)
up: Step = (-1, 0)
dn: Step = (1, 0)
lt: Step = (0, -1)
rt: Step = (0, 1)
motions = {
    '.': set(),
    'S': {up, dn, lt, rt},
    '|': {up, dn},
    '-': {lt, rt},
    'J': {lt, up},
    'F': {rt, dn},
    '7': {lt, dn},
    'L': {rt, up},
}

# Algorithm:
# - From S, check the four directions.
#  -- If two directions "work", start tracing along one of them.
#  -- Otherwise, raise an exception for now, because in practice our puzzle inputs don't do this.
#     But theoretically, you'd have to walk each path to see whether it ever loops back or dead ends.
#
# Cursor knows its position, starting at start.
# Cursor knows its *previous* position (if any).
# Cursor.move() traces the route, avoiding going backwards.
#
# Create a distance map, same size as field.

class Cursor:
    def __init__(self, field: Field, initial: Pos):
        self.field = field
        self.pos = initial
        self.last = None
        self.length = 0
        self.done = False

    def move(self, step: Step = None):
        square = field.square(*self.pos)

        if step is None:
            # Infer the direction, based on the previous move.
            if square == 'S':
                raise RuntimeError("Cannot infer direction from start square")
            directions = motions[square]
            # Find the direction that doesn't take us back to where we were before.
            step = next(iter(d for d in directions if plus(self.pos, d) != self.last))

        nextPos = plus(self.pos, step)
        nextSquare = field.square(*nextPos)

        # Determine whether the move is valid.
        valid = step in motions[square] and inverse(step) in motions[nextSquare]

        if valid:
            self.last = self.pos
            self.pos = nextPos
            self.length += 1
            print(f"pos -> {self.pos} [{self.length}]")
            # If we are not at the start square again, stop.
            if nextSquare == 'S':
                self.done = True
        else:
            self.done = True

    def looped(self):
        return self.pos == field.start() and self.length > 0

    def __str__(self):
        return str(self.pos)


def plus(p: Pos, step: Step) -> Pos:
    return tuple(x + y for x, y in zip(p, step))


def inverse(step: Step) -> Step:
    return (-step[0], -step[1])


maxLength = 0

for initialDir in (up, dn, lt, rt):
    print("--------------")
    print(f"Moving {initialDir} initially...")
    cursor = Cursor(field, field.start()); cursor.move(initialDir)
    while not cursor.done:
        cursor.move()
    print("Done.")
    print(f"Route length = {cursor.length}")
    print(f"looped? {cursor.looped()}")
    if cursor.looped() and cursor.length > maxLength: maxLength = cursor.length

print("===========")
print(f"Max length = {maxLength}")
print(f"Max distance = {maxLength // 2}")
