from fractions import Fraction as frac

def next(n):
    return 1 / n + 2

count = 0
n = frac(2, 1)
for i in range(999):
    n = next(n)
    f = 1 + 1/n
    if i < 10: print('{} / {}'.format(f.numerator, f.denominator))
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1

print(count)
