def concat_product(integer, n):
    s = ''
    for i in range(1, n + 1):
        s += str(integer * i)
    return int(s)

def pandigital(n):
    s = str(n)
    if len(s) != 9 or '0' in s: return False
    digits = set(s)
    return len(digits) == 9

v = concat_product(9, 5)
print(v)
print(pandigital(v))
print('-----')

done = False
products = set()
for integer in range(1, 10000):
    n = 1
    while True:
        product = concat_product(integer, n)
        if product > 987654321:
            break
        if pandigital(product):
            print('{} for n={} is {}'.format(integer, n, product))
            products.add(product)
        n += 1
print(max(products))
