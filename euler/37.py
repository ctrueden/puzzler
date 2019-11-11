import gmpy2

cutoff = 1000000

def crazy(p, primes):
    if p > cutoff: raise
    s = str(p)
    for d in range(1, len(s)):
        if not int(s[d:]) in primes or not int(s[:d]) in primes:
            return False
    return True

primes = set()
p = 1
while p < cutoff:
    p = gmpy2.next_prime(p)
    primes.add(int(p))

count = 0
p = 10
crazy_ones = []
while count < 11:
    p = gmpy2.next_prime(p)
    if crazy(p, primes):
        crazy_ones.append(int(p))
        count += 1

print(crazy_ones)
print(sum(crazy_ones))
