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

def digits(num):
    return sorted(str(num))

for i in range(1000, 10000):
    for j in range(1, 5000):
        i1 = i
        i2 = i + j
        if i2 > 9999: continue
        i3 = i + j + j
        if i3 > 9999: continue
        if digits(i1) != digits(i2) or digits(i1) != digits(i3): continue
        if i1 in pset and i2 in pset and i3 in pset:
            print('{} {} {}'.format(i1, i2, i3))

