import math
import numpy
from sympy.ntheory import factorint

gcds = {}
def gcd(a, b):
    global gcds
    if (a, b) in gcds: return gcds[(a, b)]
    result = math.gcd(a, b)
    gcds[(a, b)] = result
    return result

rads = {}
def rad(n):
    global rads
    if n in rads: return rads[n]
    result = numpy.prod(list(factorint(n).keys()))
    rads[n] = result
    return result

rad(20)

top = 120000
hits = []
for a in range(1, top):
    for b in range(a+1, top):
        c = a + b
        if c >= top: break
        if gcd(a, b) != 1 or gcd(a, c) != 1 or gcd(b, c) != 1:
            continue
        if rad(a*b*c) < c:
            print(f'{a} {b} {c}')
            hits.append(c)

print(len(hits))
print(sum(hits))
#print(sum(1 for i in range(top) if hits[i] > 0))
#print(sum(i for i in range(top) if hits[i] > 0))
