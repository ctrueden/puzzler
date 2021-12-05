import itertools
import logging
#logging.basicConfig(level=logging.DEBUG, format='')

class options(list):
    def __str__(self):
        # Chop off the square brackets around the list string representation.
        return "options(" + list.__str__(self)[1:-1] + ")"

count = 0
def resolve(rules, no, depth=0):
    """
    Expands the given rule to all possible terminal expressions.

    :param rules: The dict of rules, which can include both terminal and intermediate expressions.
                  A terminal expression has only literals -- e.g. `abbabaaba`.
                  An intermediate expression has 1+ rule number sequences, separated by the pipe symbol -- e.g. `1 3 2 | 4 6 7`.
    :param no: The rule number to expand.
    :return: List of terminal expressions for the desired rule number.
    """
    prefix = f"{' ' * depth}[{no}]"
    if not no in rules:
        # terminal rule!
        terminal = list(no[1]) # HACK: It's always a single letter, double quoted.
        logging.debug(f"{prefix} Terminal expression detected -- returning {terminal}")
        return terminal
    rule = rules[no]
    logging.debug(f"{prefix} Rule #{no} = {rule}")

    # NB: We store resolved lists of terminals using the list data type,
    # and unresolved intermediate expressions using the options data type.
    if type(rule) == options:
        # This is an unresolved rule. Resolve it now.
        all_terminals = []
        for option in rule:
            logging.debug(f"{prefix} Resolving option {option}")
            resolved = [resolve(rules, r, depth + 4) for r in option]
            # Now we have a list of resolved rules, each of which is a list of strings/terminals.
            # We need the product of these lists. E.g., suppose:
            # This rule option is 1 2.
            # Resolved rule 1 is ['ab', 'ba']
            # Resolved rule 2 is ['aa', 'bb']
            # 1 2 -> ['ab', 'ba'] x ['aa', 'bb'] -> ['abaa', 'abbb', 'baaa', 'babb']
            logging.debug(f"{prefix} Option {option} resolved -- {len(resolved)} possibilities")
            terminals = [''.join(t) for t in itertools.product(*resolved)]
            logging.debug(f"{prefix} Expanded {len(terminals)} terminals")
            all_terminals.extend(terminals)

        # Memoize the result: the union of each option's terminals.
        rules[no] = all_terminals

    elif type(rule) == list:
        logging.debug(f"{prefix} Rule #{no} is already resolved. Yay! {len(rule)} possible terminals.")

    return rules[no]

# Read in the rules.
with open("day19.txt") as f:
    lines = f.readlines()
rules = {}
messages = []
for line in lines:
    if ':' in line:
        r, rest = line.strip().split(': ')
        cases = options(s.split(" ") for s in rest.split(" | "))
        rules[r] = cases
    else:
        messages.append(line.strip())

# Resolve rule #0.
valid_terminals = set(resolve(rules, '0'))
print(f"Rule #0 has {len(valid_terminals)} possible terminals.")

# Check each message in our message list.
print(sum(1 for message in messages if message in valid_terminals))
