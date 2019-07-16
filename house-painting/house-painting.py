"""
You own a row of buildings along a street.

They are due for repainting, but you have no money to buy paint.
You only have leftover paint from last time: several different
colors, with some number of gallons for each.

You know the quantity of paint needed to paint each building.
According to city statutes, each building must be painted a
single color, and adjacent buildings must be different colors.
Mixing colors is not allowed.

Write a program to print which color you could paint each
building while abiding by these rules.
"""

"""
Interview Question Flow:
— Interviewer a problem
— Ask clarifying questions
— Describe an algorithm
— Choose a language and code up your algorithm
— Fix bugs / edge cases
— Describe time and space complexity

Evaluation
— Primary: Focus on getting a fully-working solution
— Secondary: Optimality in terms of big-O time/space
— Slight penalty for having bug or edge case pointed out (not discovering it yourself)
— Recorded, but not “meaningfully factored”: Code quality, how much you test, verbalizing while coding.
"""

import logging, sys

log = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s :: %(message)s'))
log.addHandler(handler)
log.setLevel(logging.INFO)


def paint(buildings, paints):
    log.info('buildings = %s', buildings)
    log.info('paints = %s', paints)
    log.info('Paint needed = %s, available = %s', sum(buildings), sum(paints))
    colors = _paint(buildings, paints, [])
    log.info('colors = %s', colors)
    return colors


def _paint(buildings, paints, colors_so_far):
    if not buildings:
        # We are done!
        # We built the colors list in reverse order, so we flip it now.
        colors_so_far.reverse()
        return colors_so_far

    remaining_buildings = buildings.copy()
    needed = remaining_buildings.pop()
    for p in range(len(paints)):
        available = paints[p]
        if available < needed:
            # Not enough paint of this color.
            continue
        if colors_so_far and colors_so_far[-1] == p:
            # Previous house is this color.
            continue
        remaining_paints = paints.copy()
        remaining_paints[p] -= needed
        colors = colors_so_far.copy()
        colors.append(p)
        result = _paint(remaining_buildings, remaining_paints, colors)
        if result:
            return result

    # No color will work from this point.
    return None


def validate(buildings, paints, colors):
    if not colors:
        return
    for b in range(len(buildings)):
        quantity = buildings[b]
        index = colors[b]
        paints[index] -= quantity
        if paints[index] < 0:
            raise Exception('Building #{} used {} of color #{}; {} remains'.format(b, quantity, index, paints[index]))
    for c in range(len(colors) - 1):
        if colors[c] == colors[c + 1]:
            raise Exception('Buildings {} and {} have the same color {}'.format(c, c + 1, colors[c]))


# -- Main --

# Try with a simple dataset.

buildings = [4, 5, 9, 7, 2, 8, 2, 12, 10, 3]
paints = [20, 9, 14, 22]
colors = paint(buildings, paints)
validate(buildings, paints, colors)

# Try with a bigger dataset.

import random
r = random.Random(0xdeadbeef)
buildings = [r.randint(2, 20) for i in range(100)]
paints = [r.randint(55, 200) for i in range(10)]
colors = paint(buildings, paints)
validate(buildings, paints, colors)

# Try with an antagonistic dataset.

sys.setrecursionlimit(10000)

buildings = [i for i in range(1, 9997)]
paints = buildings.copy()
r.shuffle(paints)
#paints.reverse()
colors = paint(buildings, paints)
validate(buildings, paints, colors)
