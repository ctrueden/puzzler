import math

def is_periodic(l, period):
    pass

def period(l):
    for i in range(len(l) / 2, 1, -1):
        if is_periodic(l, i):
            return i

def continuing_fraction(n):
    sqrt = math.sqrt(n)
    terms = []
    term = int(sqrt)
    terms.append(term)
    print(f'term = {term}')
    numer_m = 1
    numer_mod = sqrt + term
    denom = n - (term * term)
    next_term = int((sqrt + numer_mod) / denom)
    terms.append(next_term)
    print(f'next term = {sqrt + numer_mod} / {denom} = {next_term}')
    next_numer_mod = term - next_term * denom
    print(f'  + (sqrt({n}) + {next_numer_mod}) / {denom}')

    for i in range(50):
        numer_m = denom
        numer_mod = -next_numer_mod
        denom = n - next_numer_mod * next_numer_mod
        # hacky reduce; does it always work?
        denom //= numer_m
        numer_m = 1
        next_term = int(numer_m * (sqrt + numer_mod) / denom)
        terms.append(next_term)
        print(f'next term = {numer_m * (sqrt + numer_mod)} / {denom} = {next_term}')
        next_numer_mod = numer_mod - next_term * denom
        print(f'  + (sqrt({n}) + {next_numer_mod}) / {denom}')
    return terms

print(continuing_fraction(23))
