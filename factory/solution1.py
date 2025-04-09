"""
You oversee a factory with two kinds of machines.
One kind makes fizzwidgets, while the other makes thingamabobs.

* The fizzwidget machines churn out a fizzwidget every 24.75 minutes (1485 seconds).
* The thingamabob machines produce a thingamabob every 17.5 minutes (1050 seconds).

Unfortunately, the factory's power grid is rather finicky, and needs to be
frequently rebooted to avoid breaking down. To minimize such risk, you'd
ideally like to reboot often, but if you reboot while a machine is in the
middle of producing an item, that item will be ruined. You can of course
leave a machine idle some of the time to avoid such waste, but then you
lose valuable time that could have been spent producing more items.

For example, if you produce a single item with each machine, all starting
simultaneously, then reboot the power grid as soon as the fizzwidget round is
complete (after 1485 seconds), every machine in the factory will have produced
an item, but the thingamabob machines will have sat idle for 7.25 minutes
(435 seconds) after their round is finished, achieving only ~70.7% efficiency.
If you instead run the machines for 3 thingamabob rounds before rebooting the
grid, i.e. 1050*3 = 3150 seconds, the fizzwidget machines will have time for
2 rounds (1485*2 = 2970 seconds), then sit idle for only 3 minutes
(180 seconds), for an efficiency of ~94.3%.

What is the optimal time per power cycle to maximize factory efficiency?
"""

from math import lcm

from util import fancy_time

naive = 1485 * 1050
print(f"naive: {fancy_time(naive)}")

optimal = lcm(1485, 1050)
print(f"optimal: {fancy_time(optimal)}")
