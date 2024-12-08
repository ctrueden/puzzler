with open("day4.txt") as f:
    lines = f.readlines()

def grabword(matrix, x, y, xd, yd, length):
    w = ""
    for i in range(length):
        xi = x + i*xd; yi = y + i*yd
        if xi < 0 or yi < 0 or xi >= len(matrix) or yi >= len(matrix[xi]): return None
        w += matrix[xi][yi]
    return w.strip()

total = 0
target = "XMAS"
for y in range(len(lines)):
    for x in range(len(lines[y])):
        words = [
            grabword(lines, x, y, -1, -1, len(target)), # backward \ diagonal
            grabword(lines, x, y, -1, 0, len(target)), # backward horizontal
            grabword(lines, x, y, -1, 1, len(target)), # backward / diagonal
            grabword(lines, x, y, 0, -1, len(target)), # backward vertical
            grabword(lines, x, y, 0, 1, len(target)), # forward vertical
            grabword(lines, x, y, 1, -1, len(target)), # forward / diagonal
            grabword(lines, x, y, 1, 0, len(target)), # forward horizontal
            grabword(lines, x, y, 1, 1, len(target)), # forward \ diagonal
        ]
        for word in words:
            if word == target:
                total += 1
                print(f"{word} {x} {y}")

print(total)
