from decimal import *

getcontext().prec = 120

def get_sum(n):
    i = Decimal(n)
    i = i ** Decimal(.5)
    return sum(int(c) for c in str(i)[0:101] if c != '.')

import math
total = 0
for i in range(1, 101):
    root = int(math.sqrt(i))
    if root * root == i:
        continue
    total += get_sum(i)
    print(i)

print(print(total))
