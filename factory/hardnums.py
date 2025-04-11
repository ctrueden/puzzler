import random

def is_prime_miller_rabin(n, k=5):
    """
    Miller-Rabin primality test.
    
    Args:
        n: Number to test for primality
        k: Number of test rounds (higher k means lower probability of false positive)
    
    Returns:
        bool: True if n is probably prime, False if n is definitely composite
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def get_random_prime(max_value=2**30):
    """
    Generate a random prime number less than max_value.
    
    Args:
        max_value: The maximum value of the prime number (exclusive)
    
    Returns:
        int: A random prime number
    """
    while True:
        # Generate a random odd number
        n = random.randint(3, max_value - 1)
        if n % 2 == 0:
            n += 1
        
        # Test if it's prime
        if is_prime_miller_rabin(n):
            return n

#2^2*7
#2*3*5*7^2
#2^2*3*5*7^2
#2*3*5*7 = 14*15 # boring



# Example usage: print 10 random prime numbers
def main():
    product = 1
    from random import randint, choice
    primes = [get_random_prime() for _ in range(7)]
    from itertools import combinations
    p1 = choice(list(combinations(primes, 5)))
    p2 = choice(list(combinations(primes, 5)))
    prod1 = 1
    prod2 = 1
    for i in range(5):
        count1 = randint(1, 5)
        prod1 *= count1 * p1[i]
        count2 = randint(1, 5)
        prod2 *= count2 * p2[i]

    print(f"Products: {prod1} {prod2}")

    import math
    clen = math.lcm(prod1, prod2)
    from fractions import Fraction
    planck_time = Fraction(539116, 10**39)
    print(f"{clen} = {float(clen / planck_time)}")

if __name__ == "__main__":
    main()
