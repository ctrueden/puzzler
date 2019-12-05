def palindrome(n):
    s = str(n)
    return s == s[::-1]

def reverse_and_add(n):
    return n + int(str(n)[::-1])

candidates = []
for num in range(10000):
    n = num
    for iteration in range(50):
        n = reverse_and_add(n)
        if palindrome(n):
            print('Palindromic in {} iterations: {}'.format(iteration, num))
            break
    else:
        print('Not palindromic in 50 iterations: {}'.format(num))
        candidates.append(num)

print('total found: {}'.format(len(candidates)))
