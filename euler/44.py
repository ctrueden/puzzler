def penta(n):
    return n*(3*n-1)//2

bound = 10000
p = []
for i in range(bound + 1):
    p.append(penta(i))
pset = set(p)

smallest = 999999999999999999999999999999999999
smallest_j = 0
smallest_k = 0
for j in range(1, bound):
    for k in range(j + 1, bound):
        s = p[j] + p[k]
        if s not in pset: continue
        d = p[k] - p[j]
        if d not in pset: continue
        flag = ''
        if d < smallest:
            smallest = d
            smallest_j = j
            smallest_k = k
            flag = '    <============='
        print('({}, {}) = {}{}'.format(smallest_j, smallest_k, smallest, flag))
