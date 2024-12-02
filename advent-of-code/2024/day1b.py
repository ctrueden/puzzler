import re
from collections import Counter

with open("day1.txt") as f:
    lines = f.readlines()

left = []
right = []
for line in lines:
    l, r = re.split("  *", line.strip())
    left.append(int(l))
    right.append(int(r))

counter = Counter(right)

total = 0
for v in left:
    total += counter[v] * v

print(total)
