from itertools import permutations

# Concatenates digits.
def smush(nums):
    return int(''.join([str(n) for n in nums]))

def weird(digits,i,j,k,div):
    return smush([digits[i-1],digits[j-1],digits[k-1]]) % div == 0

s = 0
for digits in permutations(range(10)):
    if weird(digits,2,3,4,2) and \
       weird(digits,3,4,5,3) and \
       weird(digits,4,5,6,5) and \
       weird(digits,5,6,7,7) and \
       weird(digits,6,7,8,11) and \
       weird(digits,7,8,9,13) and \
       weird(digits,8,9,10,17):
       v = smush(digits)
       print(v)
       s += v

print('sum = ' + str(s))
