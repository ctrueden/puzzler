"""
Least Common Multiple (LCM) for rational numbers.
"""

from fractions import Fraction
from math import gcd, lcm
from random import randint


def rlcm_naive(p: Fraction, q: Fraction):
    a = p.numerator
    b = p.denominator
    c = q.numerator
    d = q.denominator
    bound = 1500 # This grows very quickly.
    best = a*b*c*d
    print(f"best -> {best}")
    for i in range(1, bound):
        pi = p*i
        #if pi >= best: break
        for j in range(1, bound):
            qj = q*j
            #if qj >= best: break
            if pi == qj and pi < best:
                print(f"best -> {pi}")
                best = pi
            #else:
            #    print(f"[{i}, {j}] {pi} != {qj}")
    return best


def rlcm_binary(p: Fraction, q: Fraction):
    return Fraction(
        lcm(p.numerator, q.numerator),
        gcd(p.denominator, q.denominator)
    )


def rlcm(*args):
    return Fraction(
        lcm(*(f.numerator for f in args)),
        gcd(*(f.denominator for f in args))
    )


def n():
    return randint(1, 99)


for p, q in (
    (Fraction(n(), n()), Fraction(n(), n())),
    (Fraction(52, 23), Fraction(25, 28)),
    (Fraction(1.23456789), Fraction(9.8642097531)),
):
    print("------------------------------------------------------")
    r = rlcm(p, q)
    print(f"p = {p} = {p.numerator/p.denominator}")
    print(f"q = {q} = {q.numerator/q.denominator}")
    print(f"rlcm({p}, {q}) = {r} = {r.numerator/r.denominator}")
    print(f"* ({r})/({p}) = {r/p}")
    print(f"* ({r})/({q}) = {r/q}")
    print(f"lcm({p.numerator}, {q.numerator}) = {lcm(p.numerator, q.numerator)}")
    print(f"gcd({p.denominator}, {q.denominator}) = {gcd(p.denominator, q.denominator)}")
    s = Fraction(lcm(p.numerator, q.numerator), gcd(p.denominator, q.denominator))
    print(f"* ({s})/({p}) = {s/p}")
    print(f"* ({s})/({q}) = {s/q}")
