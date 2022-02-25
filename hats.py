import itertools
print('hello')

# n! permutations of hats
# but how many are "all wrong"?

# if hat(i) == i, it's not "all wrong" -- throw these away (this hat(i) == i property is sometimes called "fixed")

# find all permutations where hat(0) == 0. (n-1)! of those
# then find all hat(1) == 1. (n-1)! of those
# but... some permutations of each overlap. [ where hat(0) == 0 AND hat(1) == 1 ]
# -- so we have to add those back
# -- leads to the +, -, +, -, ... pattern
# -- n! - (n-1)! + (n-2)! - (n-3)! + ... ???
# let's try it!

def count_all_wrong(n):
    count = 0
    for p in itertools.permutations(range(n)):
        for i in range(n):
            if p[i] == i:
                break
        else:
            print(p)
            count += 1
    return count


def main():
    for n in range(1, 5):
        result = count_all_wrong(n)
        print(f'{n} = {result}')

if __name__ == '__main__':
    main()
