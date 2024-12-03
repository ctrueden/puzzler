import re

with open("day3.txt") as f:
    lines = f.readlines()

instrs = []
for line in lines:
    instrs += re.findall("(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\))", line)

total = 0
active = True
for instr in instrs:
    match instr:
        case "do()":
            active = True
        case "don't()":
            active = False
        case _: # mul
            if active:
                m = re.match("mul\\(([0-9]*),([0-9]*)\\)", instr)
                a, b = int(m.group(1)), int(m.group(2))
                total += a * b

print(total)
