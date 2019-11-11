from itertools import permutations

# Concatenates digits.
def smush(nums):
    return int(''.join([str(n) for n in nums]))

products = set()

for digits in permutations(range(1, 10)):
    for i in range(1, 8):
        multiplicand = smush(digits[0:i])
        for j in range(i + 1, 9):
            multiplier = smush(digits[i:j])
            product = smush(digits[j:10])
            #print('{} x {} = {}'.format(multiplicand, multiplier, product))
            if multiplicand * multiplier == product:
                products.add(product)

print(len(products))
print(sum(products))
