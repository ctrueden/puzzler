"""
Least Common Almost Multiple (LCAM) for rational numbers.
"""

from fractions import Fraction
from math import floor, gcd, lcm
from random import randint
from typing import Sequence


def rlcm(*args):
    return Fraction(
        lcm(*(f.numerator for f in args)),
        gcd(*(f.denominator for f in args))
    )


def lcam(p: Fraction, q: Fraction, epsilon):
    """
    Calculate the Least Common Almost Multiple (LCAM) of two rational numbers
    p and q, such that m/p and m/q are both within epsilon above an integer.

    Args:
        p (Fraction or float): First rational number
        q (Fraction or float): Second rational number
        epsilon (float): Maximum allowed deviation from integers

    Returns:
        float: The LCAM value
    """
    # Convert inputs to Fraction objects if they aren't already
    p = p if isinstance(p, Fraction) else Fraction(p)
    q = q if isinstance(q, Fraction) else Fraction(q)

    # Initial guess at the exact LCM
    m = rlcm(p, q)

    # Binary search to find the smallest m that satisfies our constraints
    lower_bound = Fraction(0)
    upper_bound = Fraction(m)

    min_range = Fraction(1, 10 ** 1000)
    while upper_bound - lower_bound > min_range:  # TODO: How to bound this?
        m = (lower_bound + upper_bound) / 2
        #print(f"{lower_bound=} {upper_bound=}")

        # Check if m/p and m/q are close enough to integers
        p_div = m / p
        q_div = m / q

        p_close = 0 <= p_div - floor(p_div) <= epsilon
        q_close = 0 <= q_div - floor(q_div) <= epsilon

        if p_close and q_close:
            # If conditions are met, try a smaller m
            upper_bound = m
        else:
            # If conditions aren't met, try a larger m
            lower_bound = m

    return upper_bound  # Return the smallest valid m we found


if __name__ == "__main__":

    def n():
        return randint(1, 99)

    #p = Fraction(n(), n())
    #q = Fraction(n(), n())

    #p = Fraction(52, 23)
    #q = Fraction(25, 28)

    p = Fraction(1.23456789)
    q = Fraction(9.8642097531)

    for epsilon in \
            [Fraction(1, 10**n) for n in range(10, 1, -1)] + \
            [Fraction(1,n) for n in range(10, 1, -1)] + \
            [Fraction(10**n-1, 10**n) for n in range(1, 10)]:
        print("-------------------")
        print(f"Testing lcam at {epsilon=}")
        print("-------------------")
        result = lcam(p, q, epsilon)
        print(f"{p=}")
        print(f"LCAM of {p} and {q} with epsilon={epsilon} is {result} = {float(result)}")
        print(f"m/p = {float(result/p)}")
        print(f"m/q = {float(result/q)}")
