import math
import numpy
import gmpy2
from gmpy2 import mpz
import pickle

bound = 1000000
p = 1
print('-- Generating primes --')
primes = []
while p <= bound:
    p = gmpy2.next_prime(p)
    primes.append(p)
pset = set(primes)

#print('-- Loading factors table --')
#pfactors = pickle.load(open('pfactors.pickle', 'rb'))

# print('-- Building factors table --')
## https://stackoverflow.com/a/23712108
#def factors(n):
#    result = set()
#    n = mpz(n)
#    for i in range(1, gmpy2.isqrt(n) + 1):
#        div, mod = divmod(n, i)
#        if not mod:
#            result |= {mpz(i), div}
#    return result
#
#pfactors = {}
#for i in range(bound + 1):
#    if i % 1000 == 0:
#        print(i)
#    pfactors[i] = factors(i)
#
#pickle.dump(pfactors, open('pfactors.pickle', 'wb'))

#numfactors = {}
#def isrelativelyprime(i, j):
#    ifactors = set(pfactors[i])
#    jfactors = set(pfactors[j])
#    if not (i, j) in numfactors:
#        numfactors[(i, j)] = len(ifactors.intersection(jfactors))
#    return numfactors[(i, j)] == 1

import math
gcds = {}
def isrelativelyprime(i, j):
    if not (i, j) in gcds:
        gcds[(i, j)] = math.gcd(i, j)
    return gcds[(i, j)] == 1

print('-- Computing Totient function values --')
totient = {}
maxn = 0
maxq = 0
primeproducts = [1]
for p in primes:
    prod = primeproducts[-1] * p
    if prod > bound:
        break
    primeproducts.append(prod)
for j in primeproducts:
    totient[j] = 0
    for i in range(1, j):
        if isrelativelyprime(i, j):
            totient[j] += 1
    if totient[j] > 0:
        q = j / totient[j]
        if q > maxq:
            maxq = q
            maxn = j
            print(f'new max quotient found: n={maxn}, totient={totient[maxn]}, quotient={maxq}')

print(f'FINAL ANSWER: max n = {maxn} with totient={totient[maxn]}, quotient={maxq}')
