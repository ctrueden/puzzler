with open("day5.txt") as f:
    lines = [line.strip() for line in f.readlines()]

rules = [line.split("|") for line in lines if "|" in line]

printouts = [line.split(",") for line in lines if "," in line]

total = 0
middles = []
for printout in printouts:
    ok = True
    for before, after in rules:
        b = printout.index(before) if before in printout else -1
        a = printout.index(after) if after in printout else 99999
        if b > a:
            ok = False
            break
    if ok:
        total += 1
        middles.append(int(printout[len(printout) // 2]))

print(f"total = {total}")
print(f"middles = {middles}")
print(f"middles sum = {sum(middles)}")
