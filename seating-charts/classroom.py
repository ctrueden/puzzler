"""
Write a program to produce a seating chart for a classroom.

* Classroom desks are laid out in an evenly spaced C x R grid.

* Students learn more effectively when closer to the blackboard.
 - The blackboard is centered in front of the class.
 - Want to minimize the sum of students' distances from the blackboard.

* Some students, when seated next together, distract one another. Therefore,
  each classroom includes a list of such problematic pairs, who must not be
  seated adjacent by column, row, or diagonally.

An example:

- Classroom size: 3 columns x 4 rows
- Students: Brainy, Clumsy, Gargamel, Handy, Jokey, Papa, Smurfette, Vanity
- Problematic pairings:
    * Brainy + Jokey
    * Clumsy + Handy
    * Gargamel + anyone else

One solution:

                x
  Clumsy     Brainy      Handy
 Smurfette    Papa      Vanity
   Jokey        -          -
     -          -      Gargamel

Where "x" is the blackboard.

Follow-ups:

- What if you want all optimal solutions instead of only one?
- What if all you need is a valid solution, not necessarily optimal?
- What is the best cost function for blackboard distance?
"""


import copy, sys, time


def seating_chart(cols, rows, students, bad_pairs):
    chart = []
    for c in range(cols):
        chart.append([''] * rows)
    return _seating_chart(chart, students, bad_pairs, 0)


def _seating_chart(chart_so_far, students, bad_pairs, cost_so_far):
    if there_are_bad_pairs(chart_so_far, bad_pairs):
        # Seating chart is invalid; this path fails.
        return (None, 0)

    if not students:
        # All students seated; we are done!
        return (chart_so_far, cost_so_far)

    (bc, br, seat_cost) = best_empty_seat(chart_so_far)
    if bc is None or br is None:
        # No more seats available; this path fails.
        return (None, 0)

    next_cost = cost_so_far + seat_cost

    # Seat the student with the minimum cost.
    best_cost = 999999999999 # TODO: compute safer upper bound
    best_chart = None
    for student in students:
        # Seat the student.
        next_chart = copy.deepcopy(chart_so_far)
        next_chart[bc][br] = student
        remaining_students = [s for s in students if s != student]
        # Recurse.
        (chart, cost) = _seating_chart(next_chart, remaining_students, bad_pairs, next_cost)
        # If it's better, remember it.
        if cost < best_cost and chart is not None:
            best_cost = cost
            best_chart = chart

    if best_chart is None:
        # No one fits in the seat; burn it.
        chart_so_far[bc][br] = '-'
        return _seating_chart(chart_so_far, students, bad_pairs, cost_so_far)

    return (best_chart, best_cost)


def best_empty_seat(chart):
    cols = len(chart)
    rows = len(chart[0])
    best_cost = 99999999999 # TODO: compute safer upper bound
    best_c = None
    best_r = None
    for c in range(cols):
        for r in range(rows):
            if chart[c][r]:
                continue
            # Blackboard is centered at front of class.
            # Alternately, could do Pythagorean formula.
            cost = abs((cols - 1) / 2 - c) + r + 1
            if cost < best_cost:
                best_cost = cost
                best_c = c
                best_r = r
    return (best_c, best_r, best_cost)


def there_are_bad_pairs(chart, bad_pairs):
    cols = len(chart)
    rows = len(chart[0])
    for c in range(cols):
        for r in range(rows):
            if c and bad_pair(bad_pairs, chart[c][r], chart[c - 1][r]) or \
               r and bad_pair(bad_pairs, chart[c][r], chart[c][r - 1]) or \
               c and r and bad_pair(bad_pairs, chart[c][r], chart[c - 1][r - 1]) or \
               c and r < rows - 1 and bad_pair(bad_pairs, chart[c][r], chart[c - 1][r + 1]):
                return True
    return False


def bad_pair(bad_pairs, s1, s2):
    return s1 in bad_pairs and s2 in bad_pairs[s1] or \
           s2 in bad_pairs and s1 in bad_pairs[s2]


def print_chart(chart, empty_symbol='?'):
    if chart is None:
        print('  => EMPTY CHART <=')
        return
    cols = len(chart)
    rows = len(chart[0])
    width = 1
    for r in range(rows):
        for c in range(cols):
            width = max(width, len(chart[c][r]))
    fstr = '{:^' + str(width + 2) + '}'
    for r in range(rows):
        print()
        for c in range(cols):
            cell = chart[c][r]
            if cell == '':
                cell = empty_symbol
            sys.stdout.write(fstr.format(cell))
    print()



def assertTrue(title, condition):
    print(('[PASS]' if condition else '[FAIL]') + ' ' + title)


# -- Main --

# Input data.
cols = 3
rows = 4
students = [
    'Brainy',
    'Clumsy',
    'Gargamel',
    'Handy',
    'Jokey',
    'Papa',
    'Smurfette',
    'Vanity'
]
bad_pairs = {
    'Brainy': ['Jokey'],
    'Clumsy': ['Handy'],
    'Gargamel': ['Brainy', 'Clumsy', 'Handy', 'Jokey', 'Papa', 'Smurfette', 'Vanity']
}

# Tests.
run_tests = False
if run_tests:
    assertTrue('Handy + Clumsy BAD', bad_pair(bad_pairs, 'Handy', 'Clumsy'))
    assertTrue('Handy + Brainy OK', not bad_pair(bad_pairs, 'Handy', 'Brainy'))
    assertTrue('Brainy + Jokey BAD', bad_pair(bad_pairs, 'Brainy', 'Jokey'))
    assertTrue('Papa + Gargamel BAD', bad_pair(bad_pairs, 'Papa', 'Gargamel'))
    assertTrue('Brainy + Gargamel BAD', bad_pair(bad_pairs, 'Brainy', 'Gargamel'))
    assertTrue('Gargamel + Brainy BAD', bad_pair(bad_pairs, 'Gargamel', 'Brainy'))
    bad_chart = [
        ['Clumsy',   'Handy', 'Smurfette', '-'],
        ['Brainy',   'Papa',  'Jokey',     'Vanity'],
        ['Gargamel', '-',     '-',         '-']
    ]
    assertTrue('Bad chart is bad', there_are_bad_pairs(bad_chart, bad_pairs))
else:
    # Run the thing.
    start = time.time()
    (chart, cost) = seating_chart(cols, rows, students, bad_pairs)
    end = time.time()

    # Print the result.
    print('Elapsed: {} seconds'.format(end - start))
    print('cost = {}'.format(cost))
    if chart is None:
        print('NO CHART POSSIBLE')
    else:
        print_chart(chart, '-')
