"""
Your boss decided that measuring the machine run times to the second is NOT
EFFICIENT ENOUGH! She has ordered you to measure the runtimes as precisely as
possible (she's even a little grumpy about the 64-bit floating point precision
limit), and decide your power cycle length based on your more exact findings.
Fortunately, the automatic power cycler you designed has femtosecond precision.

So, you measure your recently upgraded fizzwidget and thingamabob machines,
and find that the more precise runtimes are actually:

* fizzwidget machines: 1319.546875 seconds
* thingamabob machines: 889.984375 seconds

Your colleague Morton independently measures too, but gets different values:

* fizzwidget machines: 1319.859375 seconds
* thingamabob machines: 889.734375 seconds

Your other colleague Wendy arrived at yet other values:

* fizzwidget machines: 1319.709283 seconds
* thingamabob machines: 889.927894 seconds

How do each of these findings affect the optimal power cycle length?

** EFFICIENCY MUST REMAIN AT 100%, NO MATTER THE RISK TO THE POWER GRID! **
"""


from util import fancy_time


def cycle_length(fizz, bob):
    # TODO: Do better!
    m = 1
    while True:
        clen = m * fizz
        bm = clen / bob
        if bm == int(bm): return clen
        m += 1


def print_combo(fizz, bob):
    cycle_len = cycle_length(fizz, bob)
    print(f"{float(fizz)} and {float(bob)}: {fancy_time(cycle_len)}")
    # Sanity checks.
    from fractions import Fraction
    fq = Fraction(str(cycle_len)) / Fraction(str(fizz))
    bq = Fraction(str(cycle_len)) / Fraction(str(bob))
    assert fq.denominator == 1, fq
    assert bq.denominator == 1, bq


print_combo(1320, 890)                # imprecise to-the-second values
print_combo(1319.546875, 889.984375)  # your measurements
print_combo(1319.859375, 889.734375)  # Morton's measurements
print_combo(1319.709283, 889.927894)  # Wendy's measurements
