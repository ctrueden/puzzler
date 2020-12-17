import numpy

#0: layer size = 6
#1: layer size = 22 = 2*(w*h + w*l + h*l)
#2: layer size = 46 = 22 + 4*(w+h+l)
#3: layer size = 78 = 
#4: layer size = 118
#4: layer size = 166

#(NOR's Cube)
#layer 0: 52
#layer 1: 88
#layer 2: 132
#layer 3: 184
#layer 4: 244

size = 100
offset = size // 2
cuboid = numpy.zeros([size, size, size], dtype=numpy.bool_)

def cell(cuboid, x, y, z):
    return cuboid[x + offset][y + offset][z + offset]

def setcell(cuboid, x, y, z):
    cuboid[x + offset][y + offset][z + offset] = 1

def grow(cuboid):
    ncuboid = numpy.zeros(cuboid.shape, dtype=cuboid.dtype)
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if cuboid[x][y][z] != 1: continue
                ncuboid[x][y][z] = 1
                ncuboid[x-1][y][z] = 1
                ncuboid[x+1][y][z] = 1
                ncuboid[x][y-1][z] = 1
                ncuboid[x][y+1][z] = 1
                ncuboid[x][y][z-1] = 1
                ncuboid[x][y][z+1] = 1
    return ncuboid

def populate(cuboid, w, h, l):
    for x in range(w):
        for y in range(h):
            for z in range(l):
                setcell(cuboid, x, y, z)

def shape_size(cuboid):
    return sum(c for c in numpy.nditer(cuboid))


goal = 1000
top = 200000
C = [0] * top
for w in range(1,top):
    if w*w*w>=top: break
    for h in range(w,top):
        print(f'Processing {w} x {h}')
        if w*w*h>=top: break
        for l in range(h,top):
            if w*h*l>=top: break
            cubes = 2*(w*h + w*l + h*l)
            if cubes >= top: break
            C[cubes] += 1
            inc = 4*(w+h+l)
            cubes += inc
            while cubes < top:
                C[cubes] += 1
                inc += 8
                cubes += inc

for i in range(0, top):
    if C[i] == goal:
        print(f'C({i}) = {C[i]}')
        break

"""
populate(cuboid, 1, 2, 3)
total_size = []
for g in range(5):
    print(f'{g}')
    total_size.append(shape_size(cuboid))
    cuboid = grow(cuboid)
total_size.append(shape_size(cuboid))

for g in range(4):
    print(f'layer {g}: {total_size[g+1] - total_size[g]}')
"""
