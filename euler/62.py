import collections
cubes = []
hist = []
num = 999
for i in range(num):
    cube = i ** 3
    cubes.append(cube)
    hist.append(collections.Counter(str(cube)))

for i in range(num):
    for j in range(i + 1, num):
        for k in range(j + 1, num):
            if hist[i] == hist[j] and hist[i] == hist[k]:
                print(f'triple: {cubes[i]} {cubes[j]} {cubes[k]}')
#            for l in range(k + 1, num):
#                if hist[i] == hist[j] and hist[i] == hist[k] and hist[i] == hist[l]:
#                    print(f'quadruple: {cubes[i]} {cubes[j]} {cubes[k]} {cubes[l]}')
#                for m in range(l + 1, num):
#                    if hist[i] == hist[j] and hist[i] == hist[k] and hist[i] == hist[l] and hist[i] == hist[m]:
#                        print(f'quintuple: {cubes[i]} {cubes[j]} {cubes[k]} {cubes[l]} {cubes[m]}')
print(hist)
