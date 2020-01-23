import math
import gmpy2

from itertools import combinations

#bound = 987654
bound = 10000000
p = 1
print('-- Generating primes --')
primes = []
while p <= bound:
    p = gmpy2.next_prime(p)
    primes.append(int(p))
pset = set(primes)

def remarkable(combo):
    for pair in combinations(combo, 2):
        v = int(str(pair[0]) + str(pair[1]))
        if not v in pset: return False
        v = int(str(pair[1]) + str(pair[0]))
        if not v in pset: return False
    return True

for p in primes:
    for i in range(1, len(p)):
        # split prime in half
        # see if both halves are prime
        # is this even helpful

"""
print('-- Trying brute force --')
best = (99999999, 9999999, 9999999, 9999999, 9999999)
for combo in combinations(primes, 5):
    if remarkable(combo):
        print(combo)
        if sum(combo) < sum(best):
            best = combo
            print('---> NEW BEST: {}'.format(combo))

print('-- Trying something dumb --')
t = [3, 7, 109, 673, 2]
best = (99999999, 9999999, 9999999, 9999999, 9999999)
for p in primes:
    t[4] = p
    if remarkable(t):
        print(t)
        if sum(t) < sum(best):
            best = t
            print('---> NEW BEST: {}'.format(t))
"""
