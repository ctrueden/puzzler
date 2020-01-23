from fractions import Fraction as frac

def find_closest_to_three_sevenths(bound):
    fracs = set()
    three_sevenths = frac(3, 7)
    for d in range(2, bound + 1):
        if d % 100 == 0: print(d)
        # d = 3 * n / 7
        # n = d * 7 // 3
        n = d * 3 // 7
        f = frac(n, d)
        fracs.add(f)

    lfrac = list(fracs)
    lfrac.sort()
    #print([str(f) for f in lfrac])
    return lfrac[-2]

bound = 1000000
#for bound in range(4, 10000, 50):
result = find_closest_to_three_sevenths(bound)
print(f'{bound} = {result}')
