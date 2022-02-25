import itertools
from math import factorial as fac

# n! permutations of hats
# but how many are "all wrong"?

# What is the probability that the result will be all wrong?

# if hat(i) == i, it's not "all wrong" -- throw these away (this hat(i) == i property is sometimes called "fixed")

# find all permutations where hat(0) == 0. (n-1)! of those
# then find all hat(1) == 1. (n-1)! of those
# but... some permutations of each overlap. [ where hat(0) == 0 AND hat(1) == 1 ]
# -- so we have to add those back
# -- leads to the +, -, +, -, ... pattern
# -- n! - (n-1)! + (n-2)! - (n-3)! + ... ???
# let's try it!

def formula(n):
    # GOAL:
    # 1 = 0
    # 2 = 1
    # 3 = 2
    # 4 = 9
    # 5 = 44
    # 6 = 265
    # 7 = 1854
    # 8 = 14833
    # 9 = 133496
    return formula(n-1) * n + (-1)**n if n > 1 else 0


def count_all_wrong(n):
    count = 0
    for p in itertools.permutations(range(n)):
        for i in range(n):
            if p[i] == i:
                break
        else:
            #print(p)
            count += 1
    return count


def main():
    for n in range(1, 10):
        all_wrong = count_all_wrong(n)
        f = formula(n)
        assert all_wrong == f
        prob = all_wrong / fac(n)
        print(f'{n} = {all_wrong} (formula says {f}) -- probability is {prob}')

if __name__ == '__main__':
    main()

# "all wrong" is commonly known as a derangement. Or a subfactorial. Typically written !n instead of n!.
# !N = N! * [1 − 1/!1 + 1/2! - 1/3! + 1/4! - ... + 1/N!]
