import math
import gmpy2

bound = 999999
p = 1
print('-- Generating primes --')
primes = []
while p <= bound:
    p = gmpy2.next_prime(p)
    primes.append(p)
pset = set(primes)

print('-- Checking families --')
count = 0
for p in primes:
    if count % 100 == 0: print('Checking prime {}'.format(p))
    count += 1
    num_digits = len(str(p))
    digits = num_digits * [0]
    pattern = num_digits * ['']
    # NB: Starting i at 1 ensures at least 1 digit is replaced.
    for i in range(0, 2**num_digits):
        remain = i
        for d in range(num_digits):
            bit = remain % 2 == 1
            remain //= 2
            # Replace this digit with new_digit if active bit.
            pattern[d] = 'x' if bit else '-'
#        print('Checking prime {} with pattern {}:'.format(p, pattern), end=' ')

        matching_primes = set()
        for new_digit in range(0, 10):
            remain = i
            for d in range(num_digits):
                bit = remain % 2 == 1
                remain //= 2
                # Replace this digit with new_digit if active bit.
                digits[num_digits - d - 1] = new_digit if bit else int(str(p)[d])
            modified_num = int(''.join(str(d) for d in digits)[::-1])
            if modified_num in pset and len(str(modified_num)) == len(str(p)):
#                print('{}({})'.format(modified_num, i), end=' ')
                matching_primes.add(modified_num)
                if len(matching_primes) == 7:
                    # FOUND IT
                    print()
                    print('GETTING CLOSE: {} with pattern {}: {}'.format(p, pattern, matching_primes))
                if len(matching_primes) == 8:
                    # FOUND IT
                    print()
                    print('WE FOUND IT: {} with pattern {}: {}'.format(p, pattern, matching_primes))
                    import sys; sys.exit()
#        print()
