import math

def choose(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

count = 0
nlist = []
for n in range(1, 101):
    for r in range(1, n + 1):
        result = choose(n, r)
        if result > 1000000:
            print('{} choose {} = {}'.format(n, r, result))
            count += 1
            nlist.append((n, r))
print(nlist)
print(count)
