def tri(n):
    return n*(n+1)//2

def penta(n):
    return n*(3*n-1)//2

def hexa(n):
    return n*(2*n-1)

print('{} = {} = {} = 40755'.format(tri(285), penta(165), hexa(143)))

t = []
p = []
h = []
for i in range(100000):
    t.append(tri(i))
    p.append(penta(i))
    h.append(hexa(i))

ts = set(t)
ps = set(p)
hs = set(h)

for i in range(100000):
    if t[i] in ps and t[i] in hs:
        print('{} :: {}'.format(i, t[i]))
