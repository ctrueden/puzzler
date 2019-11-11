import gmpy2

def circular(n, s):
    # This function courtesy of NOR.
    ns = str(n)
    for i in range(len(ns)):
        rotation = ns[i:] + ns[:i]
        rn = int(rotation)
        if rn not in s: return False
    return True

primes = set()
p = 1
while p < 1000000:
    p = gmpy2.next_prime(p)
    primes.add(int(p))

circ = [p for p in primes if circular(p, primes)]
print('{} : {}'.format(len(circ), circ))
