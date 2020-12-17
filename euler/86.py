from functools import reduce

def factors(n):
    return [[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0]

print(factors(12))
