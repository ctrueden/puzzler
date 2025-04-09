"""
After a costly power grid failure brought on by insufficiently frequent power
cycling, your boss relents and says she is willing to tolerate machines sitting
idle for VERY SMALL amounts of time, as long as it reduces future grid failure
incidents by greatly improving the power cycling time.

Efficiency must still not drop below FIVE NINES (99.999%) for any machine in
the factory, as measured by the ratio (machine_active_runtime / cycle_length).

Your measured runtime values:
* fizzwidget machines: 1319.546875 seconds
* thingamabob machines: 889.984375 seconds

Morton's measured runtime values:
* fizzwidget machines: 1319.859375 seconds
* thingamabob machines: 889.734375 seconds

Wendy's measured runtime values:
* fizzwidget machines: 1319.709283 seconds
* thingamabob machines: 889.927894 seconds

Find the shortest power cycle length within the FIVE NINES constraint,
along the corresponding efficiency rating.

For good measure, find the same within 99.99%, 99.9%, 99%, and 90%,
to help your boss make a decision around risk tolerance vs. efficiency.
"""

from fractions import Fraction
from math import floor, gcd, lcm

from util import fancy_time


def rlcm(*args):
    return Fraction(
        lcm(*(f.numerator for f in args)),
        gcd(*(f.denominator for f in args))
    )


def efficiency(fizz, bob, cycle_len):
    fizz_count = floor(cycle_len / fizz)
    bob_count = floor(cycle_len / bob)
    return Fraction(min(fizz_count * fizz, bob_count * bob) / cycle_len)


def best_cycle(fizz, bob, cutoff):
    # TODO: Write this function!
    return (0, 0)


def report(fizz, bob, cutoff):
    cycle_len, eff = best_cycle(fizz, bob, cutoff)
    print(f"{fizz} and {bob} --> [{float(100*eff)}%] {float(cycle_len)} seconds")


print(f"--- 100% ---")
for fizz, bob in (
    (1319.546875, 889.984375), # you
    (1319.859375, 889.734375), # Morton
    (1319.709283, 889.927894), # Wendy
):
    print(f"{fizz} and {bob} --> {fancy_time(rlcm(Fraction(fizz), Fraction(bob)))}")

for cutoff in [0.99999, 0.9999, 0.999, 0.99, 0.9]:
    print()
    print(f"--- {100*cutoff:.5g}% ---")
    report(1319.546875, 889.984375, cutoff)  # your measurements
    report(1319.859375, 889.734375, cutoff)  # Morton's measurements
    report(1319.709283, 889.927894, cutoff)  # Wendy's measurements
