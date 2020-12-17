import itertools

def can_multiply(k, available):
    print(f'can_multiply({k}, {available})?')
    if k == 1 or k in available:
        print('--> base case: True')
        return True
    for x in available:
        if can_multiply(x, available) and can_multiply(k - x, available):
            print('--> works for ')
            return True
    return False

def min_multiply(k):
    for mk in range(1, k-1):
        for available in itertools.combinations(range(2, k-1), mk):
            if can_multiply(k, available):
                print(f'{available}')
                return mk

print(min_multiply(15))
