import collections, math

triangles = collections.defaultdict(list)

for a in range(1, 501):
    for b in range(a, 501):
        c = math.sqrt(a*a + b*b)
        if c != int(c): continue
        c = int(c)
        p = a + b + c
        if p > 1000: break
        triangles[p].append((a, b, c))

max_p = 0
max_len = 0

for p, v in triangles.items():
    if len(v) > max_len:
        max_p = p
        max_len = len(v)
        print(f"{p} -> {max_len}: {v})")
