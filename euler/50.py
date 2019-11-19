import math
import gmpy2

bound = 999999
p = 1
print('-- Generating primes --')
primes = []
while p <= bound:
    p = gmpy2.next_prime(p)
    primes.append(p)
pset = set(primes)

best = 0
for start in range(len(primes)):
#    print('-- Starting at {} --'.format(primes[start]))
    for length in range(best, len(primes)):
        total = sum(primes[p] for p in range(start, start+length))
        if total > 1000000: break
        if total in pset:
            print('len={} total={} first_prime={}'.format(length, total, primes[start]))
            best = length
