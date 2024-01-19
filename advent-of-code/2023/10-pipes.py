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

print(lines)

class Field:
    def __init__(self, lines):
        self.lines = lines

    def start(self) -> tuple[int, int]:
        for i, line in enumerate(self.lines):
            s = line.find("S")
            if s >= 0: return i, s
        raise RuntimeError("THERE IS NO START WTF")

field = Field(lines)

print(field.start())
