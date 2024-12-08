with open("day4.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def mas(word):
    return word == "MAS" or word == "SAM"

total = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[y]) - 1):
        c = lines[y][x]
        tl = lines[y-1][x-1]
        tr = lines[y-1][x+1]
        bl = lines[y+1][x-1]
        br = lines[y+1][x+1]
        slash = bl + c + tr
        backslash = tl + c + br
        if mas(slash) and mas(backslash): total += 1

print(total)
