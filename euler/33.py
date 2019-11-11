def good(expected, numer, denom):
    return denom != 0 and expected == numer/denom

def curious_fraction(a, b):
    a_ten = a // 10
    a_one = a % 10
    b_ten = b // 10
    b_one = b % 10
    if (a_one == 0 and b_one == 0) or \
       (a_ten == 0 and b_ten == 0):
        # trivial
        return False
    if (a_one == b_one and good(a/b, a_ten, b_ten)) or \
       (a_one == b_ten and good(a/b, a_ten, b_one)) or \
       (a_ten == b_one and good(a/b, a_one, b_ten)) or \
       (a_ten == b_ten and good(a/b, a_one, b_one)):
        print('{} / {}'.format(a, b))
        return True

numer = 1
denom = 1
for a in range(100):
    for b in range(a+1, 100):
        if curious_fraction(a, b):
            numer *= a
            denom *= b

print('{} / {}'.format(numer, denom))

