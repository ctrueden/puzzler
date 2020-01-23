from math import factorial as fac

def fac_sum(n):
    return sum(fac(int(d)) for d in str(n))

#print(fac_sum(145))

def chain_count(n):
    values = set()
    values.add(n)
    while True:
        v = fac_sum(n)
        if v in values:
            break
        values.add(v)
        n = v
    return len(values)

#print(chain_count(69))

num = 0
for n in range(1, 1000001):
    if chain_count(n) == 60:
        print(n)
        num += 1

print(f'TOTAL: {num}')
