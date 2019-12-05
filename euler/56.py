def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print(max(sum_digits(a ** b) for a in range(100) for b in range(100)))
