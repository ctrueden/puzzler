"""
Count from 1 to 2000 using "clever" roman numerals: not the traditional
digit-by-digit encoding, but the shortest string of roman numeral symbols
that evaluates to the target number under the standard left-to-right
evaluation rule (each symbol adds its value, unless it is immediately
followed by a strictly larger symbol, in which case it subtracts) -- subject
to a few extra well-formedness rules that keep the result from being a
free-for-all:

  - V, L, D may each appear at most once in the whole numeral (two of them
    would just be the next symbol up: DD == M, so use that instead).
  - I, X, C, M may repeat, but at most 3 times in a row additively (as in
    classic roman numerals).
  - A subtraction is a single symbol immediately before a larger one (XM,
    IM, CD, ...) -- never a chain of two smaller symbols subtracted in a
    row (IVM, i.e. "M - V - I", is not allowed).
  - Only the *final* (rightmost) occurrence of a given symbol may be the
    target of a subtraction. E.g. MXMIII (M, then XM, then III) is fine
    because only the second, final, M is reduced -- but IVMIM and VMXM are
    not, because they'd reduce an M that isn't the last one.

E.g. 1993 is traditionally MCMXCIII (8 symbols); under these relaxed rules
the shortest is MXMIII (6 symbols): M=1000, X<M so -10, M=+1000, I=+1,
I=+1, I=+1 => 1000 - 10 + 1000 + 3 = 1993.
"""

from collections import deque

VALUES = [1, 5, 10, 50, 100, 500, 1000]
SYMBOL = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
BIT = {v: i for i, v in enumerate(VALUES)}
REPEATABLE = {1, 10, 100, 1000}   # I, X, C, M: may repeat (max 3 in a row)
SINGLE = {5, 50, 500}             # V, L, D: at most once in the whole numeral

LIMIT = 2000
MAX_LEN = 16

# A state describes the leftmost character of the suffix built so far
# (we build right-to-left, prepending characters):
#   total       -- value of the suffix under the evaluation rule
#   lval        -- value of the current leftmost character
#   is_sub      -- does the leftmost character subtract from its right
#                  neighbor? (needed to forbid chained subtraction)
#   eligible    -- is the leftmost character the *final* (rightmost)
#                  occurrence of its value, i.e. can something to its left
#                  legally subtract from it?
#   seen        -- bitmask of which values have appeared anywhere in the
#                  suffix so far
#   run         -- length of the consecutive same-value run ending at the
#                  leftmost character (for the "max 3 in a row" rule)

Start = {}  # state -> (length, symbol_prepended, prev_state)
for v in VALUES:
    state = (v, v, False, True, 1 << BIT[v], 1)
    Start[state] = (1, None, None)

queue = deque(Start.keys())
best_for_sum = {}


def maybe_record(total, length, state):
    if 1 <= total <= LIMIT and total not in best_for_sum:
        best_for_sum[total] = (length, state)


for state in queue:
    length, _, _ = Start[state]
    maybe_record(state[0], length, state)

while queue and len(best_for_sum) < LIMIT:
    state = queue.popleft()
    length, _, _ = Start[state]
    if length >= MAX_LEN:
        continue
    total, lval, is_sub, eligible, seen, run = state

    for v in VALUES:
        if v in SINGLE and (seen & (1 << BIT[v])):
            continue  # V, L, D: at most once in the whole numeral

        subtracting = v < lval
        if subtracting:
            if is_sub or not eligible:
                continue  # chained subtraction, or target isn't the final occurrence
            new_run = 1
        else:
            if v == lval:
                if v in REPEATABLE:
                    new_run = run + 1
                    if new_run > 3:
                        continue
                else:
                    new_run = 1  # unreachable: SINGLE values already excluded above
            else:
                new_run = 1

        new_total = total + (-v if subtracting else v)
        new_seen = seen | (1 << BIT[v])
        new_eligible = not (seen & (1 << BIT[v]))
        new_state = (new_total, v, subtracting, new_eligible, new_seen, new_run)

        if new_state in Start:
            continue
        Start[new_state] = (length + 1, v, state)
        maybe_record(new_total, length + 1, new_state)
        queue.append(new_state)


def reconstruct(state):
    symbols = []
    while state is not None:
        length, sym, prev = Start[state]
        symbols.append(SYMBOL[sym] if sym is not None else SYMBOL[state[1]])
        state = prev
    return "".join(symbols)


for n in range(1, LIMIT + 1):
    length, state = best_for_sum[n]
    print(f"{n}\t{reconstruct(state)}")
