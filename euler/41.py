import gmpy2

def pandigital(n):
    s = str(n)
    digits = set(s)
    for i in range(1, len(str(n)) + 1):
        if not str(i) in digits: return False
    return True

p = 1
while p <= 987654321:
    p = gmpy2.next_prime(p)
    if pandigital(p):
        print(p)
