limit = 1000
#limit = 3
minn = 12
maxn = 1000000
for n in range(minn, maxn):
    print(f'[{n}]')
    k = 1
    hits = 0
    # 1/n = 1/x + 1/y
    #  --> 1/n = k/kn
    #  --> k/kn = (k-1+1)/kn = (k-1)/kn + (1)/kn
    #  --> k/kn = (k-1)/kn + 1/kn
    # SUPPOSE 1/kn = 1/y   -->  y=kn
    #  --> BUT CONJECTURE IS FALSE: e.g. 1/12 = 1/21 + 1/28
    # 1/y = 1/kn
    # 1/x = (k-1)/kn
    # y = kn
    # x = kn/(k-1)
    x = n + 2 # Force first iteration.
    while x > n + 1: # ???
        k += 1
        if k*n % (k-1) == 0:
            hits += 1
            x = (k*n) // (k-1)
            y = k*n
            #print(f'1/{x} + 1/{y} = 1/{n}')
        if hits >= limit:
            print(f'SUCCESS! n={n}')
            break
    print(hits)
    if hits >= limit:
        break

# 8 solutions for n=12:
# 1 / (2*2*3) = (1 / 13) + (1 / (2*2*3*13))
# 1 / (2*2*3) = (1 / (2*7)) + (1 / (2*2*3*7))
# 1 / (2*2*3) = (1 / (3*5)) + (1 / (2*2*3*5))
# 1 / (2*2*3) = (1 / (2*2*2*2)) + (1 / 2*2*2*2*3)
# 1 / (2*2*3) = (1 / (2*3*3)) + (1 / (2*2*3*3))
# 1 / (2*2*3) = (1 / (2*2*5)) + (1 / (2*3*5))
# 1 / (2*2*3) = (1 / (3*7)) + (1 / (2*2*7))
# 1 / (2*2*3) = (1 / (2*2*2*3)) + (1 / (2*2*2*3))
