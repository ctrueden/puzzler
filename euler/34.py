import math

def curious_number(n):
    total = sum(math.factorial(int(d)) for d in str(n))
    return total == n

grand_total = 0
for i in range(10, 10000000):
    if curious_number(i):
        print(i)
        grand_total += i

print('grand total = {}'.format(grand_total))
