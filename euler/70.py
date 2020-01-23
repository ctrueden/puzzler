from math import gcd

def perm(a, b):
    sa = list(str(a))
    sa.sort()
    sb = list(str(b))
    sb.sort()
    return sa == sb

# From https://www.geeksforgeeks.org/eulers-totient-function/

# A simple method to evaluate 
# Euler Totient Function 
def phi(n): 
    # Initialize result as n 
    result = n;  
  
    # Consider all prime factors 
    # of n and subtract their 
    # multiples from result 
    p = 2;  
    while(p * p <= n): 
          
        # Check if p is a  
        # prime factor. 
        if (n % p == 0):  
              
            # If yes, then  
            # update n and result 
            while (n % p == 0): 
                n = int(n / p); 
            result -= int(result / p); 
        p += 1; 
  
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most  
    # one such prime factor) 
    if (n > 1): 
        result -= int(result / n); 
    return result; 

# Driver Code 
min_ratio = 10000
min_n = -1
for n in range(10000000, 1, -1): 
    p = phi(n)
    if not perm(n, p):
        continue
    ratio = n / p
    if ratio < min_ratio:
        min_ratio = ratio
        min_n = n
        print(f'New minimum: {min_n} / {p} = {min_ratio}')
