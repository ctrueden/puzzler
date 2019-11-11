import math
for p in range(1, 1001):
    for a in range(1, 1001):
        for b in range(1, 1001 - a):
            c = math.sqrt(a*a + b*b)
            if c != int(c):
                continue
            c = int(c)
            if a+b+c == p:
                print('p={} :: {} {} {}'.format(p, a, b, c))

