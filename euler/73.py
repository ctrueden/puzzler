from fractions import Fraction as frac
import math

def isrelativelyprime(i, j):
    return math.gcd(i, j) == 1

fracs = set()
bound = 12000
one_half = frac(1, 2)
one_third = frac(1, 3)
for d in range(2, bound + 1):
    if d % 50 == 0: print(d)
    for n in range(1, d):
#        if isrelativelyprime(n, d):
        f = frac(n, d)
        if f > one_third and f < one_half:
            fracs.add(f)

print(len(fracs))
