from itertools import combinations
import math

def tri(n):
    return n*(n+1)//2

def square(n):
    return n**2

def penta(n):
    return n*(3*n-1)//2

def hexa(n):
    return n*(2*n-1)

def hepta(n):
    return n*(5*n-3)//2

def octa(n):
    return n*(3*n-2)

def cyclic(v):
    pass


n3 = list([tri(n) for n in range(10000) if tri(n) >= 1000 and tri(n) <= 9999])
n4 = list([square(n) for n in range(10000) if square(n) >= 1000 and square(n) <= 9999])
n5 = list([penta(n) for n in range(10000) if penta(n) >= 1000 and penta(n) <= 9999])
n6 = list([hexa(n) for n in range(10000) if hexa(n) >= 1000 and hexa(n) <= 9999])
n7 = list([hepta(n) for n in range(10000) if hepta(n) >= 1000 and hepta(n) <= 9999])
n8 = list([octa(n) for n in range(10000) if octa(n) >= 1000 and octa(n) <= 9999])

print(len(n3) * len(n4) * len(n5) * len(n6) * len(n7) * len(n8))

def good(pre, post, nums):
    if len(nums) == 0:
        return True
    return False
    


def pre(n):
    return 0

def post(n):
    return 0

for i3 in n3:
    for i4 in n4:
        for i5 in n5:
            for i6 in n6:
                for i7 in n7:
                    for i8 in n8:
                        nums = [i3, i4, i5, i6, i7, i8]
#                        for i in range(nums):
#                            if good(pre(n), post(n), nums - n)
#                        if good():
#                            print('{i3} {i4} {i5} {i6} {i7} {i8}')

