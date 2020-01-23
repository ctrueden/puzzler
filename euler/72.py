from fractions import Fraction as frac
import math

def isrelativelyprime(i, j):
    return math.gcd(i, j) == 1

fracs = set()
bound = 1000000
for d in range(2, bound + 1):
    if d % 50 == 0: print(d)
    for n in range(1, d):
        if isrelativelyprime(n, d):
            fracs.add(frac(n, d))

print(len(fracs))
