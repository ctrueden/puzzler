#from collections import Counter

def good(n):
    digits = sorted(str(n)) # Counter
    for mul in range(2, 7):
        if digits != sorted(str(mul*n)): # Counter
            return False
    return True

digits = 6
mn = 10**(digits-1)
mx = 2 * mn
print(f"searching {mn} - {mx}...")
for i in range(mn, mx):
    if good(i):
        print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
        break
