import math
import gmpy2

bound = 987654
p = 1
print('-- Generating primes --')
primes = []
while p <= bound:
    p = gmpy2.next_prime(p)
    primes.append(p)
pset = set(primes)

print('-- Checking composites --')
for i in range(9, bound, 2):
    if i in pset: continue # skip prime number
    found = False
    for p in primes:
        if p > i: break
        twice_square = math.sqrt((i - p) / 2)
        if twice_square == int(twice_square):
            print('{} = {} + 2x{}^2'.format(i, p, int(twice_square)))
            found = True
            break
    if not found:
        print('{}  <-- CANNOT. DONE'.format(i))
        break

