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
    lines = f.readlines()

Pos = tuple[int, int]
Step = tuple[int, int]

class Field:
    def __init__(self, lines):
        self.lines = lines

    def start(self) -> Pos:
        for i, line in enumerate(self.lines):
            s = line.find("S")
            if s >= 0: return i, s
        raise RuntimeError("THERE IS NO START WTF")

    def square(self, row, col):
        rowCount = len(lines)
        colCount = len(lines[0]) # NB: Assumes same-length lines.
        return (
            '.'
            if row < 0 or row >= rowCount or col < 0 or col >= colCount
            else
            lines[row][col]
        )

field = Field(lines)

print(field.start())

# NB: Coordinates are (y, x) -- i.e. (vertical, horizontal) -- i.e. (row, col)
up: Step = (-1, 0)
dn: Step = (1, 0)
lt: Step = (0, -1)
rt: Step = (0, 1)
motions = {
    'S': {up, dn, lt, rt},
    '|': {up, dn},
    '-': {lt, rt},
    'J': {lt, up},
    'F': {rt, dn},
    '7': {lt, dn},
    'L': {rt, up},
}

def valid(square1: str, square2: str):
    return len(motions[square1] & motions[square2]) > 0

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

    def move(self, direction: Step = None):
        square = field.square(*self.pos)

        if direction is None:
            # Infer the direction, based on the previous move.
            if square == 'S':
                raise RuntimeError("Cannot infer direction from start square")
            directions = motions[square]
            # Find the direction that doesn't take us back to where we were before.
            direction = next(iter(d for d in directions if d != self.last))

        nextPos = plus(self.pos, direction)
        nextSquare = field.square(*nextPos)
        if valid(square, nextSquare):
            self.last = self.pos
            self.pos = nextPos
            self.length += 1
            # If we are not at the start square again, stop.
            if nextSquare == 'S':
                self.done = True
        else:
            self.done = True

    def looped(self):
        return self.pos == field.start() and self.length > 0

    def __str__(self):
        return str(self.pos)

def plus(p1: Pos, p2: Pos):
    return tuple(x + y for x, y in zip(p1, p2))

for initialDir in (up, dn, lt, rt):
    print(f"Moving {initialDir} initially...")
    cursor = Cursor(field, field.start()); cursor.move(initialDir)
    while not cursor.done:
        cursor.move()
    print("Done.")
    print(cursor.looped())
    print(cursor.length)
    print("------------")
