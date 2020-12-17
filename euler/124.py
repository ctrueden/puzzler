import gmpy2

p = 1
primes = []
while p < 1000:
    p = gmpy2.next_prime(p)
    primes.append(int(p))

def rad(n):
    product = 1
    for f in factors(n):
        product *= f
    return product

def factors(n):
    p = 0
    limit = n//2
    factors = []
    while primes[p] < limit:
        if n % primes[p] == 0:
            factors.append(primes[p])
    return factors

print(factors(10))
