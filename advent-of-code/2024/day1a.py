import re

with open("day1.txt") as f:
    lines = f.readlines()

left = []
right = []
for line in lines:
    l, r = re.split("  *", line.strip())
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

total = 0
for l, r in zip(left, right):
    total += abs(l - r)

print(total)
