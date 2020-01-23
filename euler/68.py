import itertools
solutions = []
for p in itertools.permutations(range(1, 11), 10):
    # 012, 324, 546, 768, 981
    #if p[0] < 6:
    #    continue
    if p[0] > p[3] or p[0] > p[5] or p[0] > p[7] or p[0] > p[9]:
        continue
    value = p[0] + p[1] + p[2]
    if value != p[3] + p[2] + p[4] or value != p[5] + p[4] + p[6] or value != p[7] + p[6] + p[8] or value != p[9] + p[8] + p[1]:
       continue
    s = f'{p[0]}{p[1]}{p[2]}{p[3]}{p[2]}{p[4]}{p[5]}{p[4]}{p[6]}{p[7]}{p[6]}{p[8]}{p[9]}{p[8]}{p[1]}'
    if len(s) == 16:
        solutions.append(s)

print(max(solutions))
