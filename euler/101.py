from sympy import Symbol, interpolating_poly, poly
#from numpy import polyfit as pf, poly1d as poly

#x = [1, 2, 3, 4]
#y = [1, 8, 27, 64]

def f(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

x = list(range(1, 16))
y = [f(n) for n in range(1, 16)]

var = Symbol('x')

total = 0
for n in range(1, len(x)):
    #coeffs = pf(x[0:n], y[0:n], n-1)
    p = interpolating_poly(n, var, x[0:n], y[0:n])
    ###
    #coeffs = [p.subs(var, v) for v in x[0:n]]
    #p = poly(coeffs)
    #v = p(n+1)
    v = p.subs(var, n+1)
    print(f'{p.expand()} for n={n+1} -> {v}')
    if v != y[n]:
        print(f'------> WRONG: {y[n]}')
        total += v

print(total)

