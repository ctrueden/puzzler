"""
You're looking to upgrade your machines, since it's been awhile.
There are various newer, better, more awesome fizzwidget and thingamabob
machine models on the market these days, each of which produces items at a
different rate. To help you decide what to buy, you would like to know,
for a given prospective fizzwidget model and thingamabob model, what the
optimal power cycle efficiency would be with that combination.

For example, if you upgrade the fizzwidget machines to ones that run in
1234 seconds, and the thingamabob machines to ones that run in 890 seconds,
how would it affect the factory's power cycle efficiency?

What about 1320 for fizzwidgets and 890 for thingamabobs? Or 1234 and 1008?
How about 1320 and 1008? 1234 and 890? Which combination would be best?
"""


from util import fancy_time


def cycle_length(fizz, bob):
    # TODO: Do better! This is just an upper bound.
    return fizz * bob


def print_combo(fizz, bob):
    print(f"{fizz:4} and {bob:4}: {fancy_time(cycle_length(fizz, bob))}")


# current machines
print_combo(1485, 1050)

# candidate new machines
print_combo(1320, 890)
print_combo(1234, 1008)
print_combo(1320, 1008)
print_combo(1234, 890)
