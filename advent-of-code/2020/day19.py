import itertools
import logging
#logging.basicConfig(level=logging.DEBUG, format='')

shiftwidth = 4

class options(list):
    def __str__(self):
        # Chop off the square brackets around the list string representation.
        return "options(" + list.__str__(self)[1:-1] + ")"

def resolve(rules, no, maxlen=float("inf"), depth=0):
    """
    Expands the given rule to all possible terminal expressions.

    :param rules: The dict of rules, which can include both terminal and unresolved expressions.
                  A terminal expression has only literals -- e.g. `abbabaaba`.
                  An unresolved expression has 1+ options (rule number sequences),
                  separated by the pipe symbol -- e.g. `1 3 2 | 4 6 7`.
    :param no: The rule number to expand.
    :return: List of terminal expressions for the desired rule number.
    """
    prefix = f"{' ' * (shiftwidth*depth)}[{no}]"
    if not no in rules:
        # terminal rule!
        terminal = list(no[1]) # HACK: It's always a single letter, double quoted.
        logging.debug(f"{prefix} Terminal expression detected -- returning {terminal}")
        return terminal
    rule = rules[no]
    logging.debug(f"{prefix} Rule #{no} = {rule}")

    # NB: We store a resolved collection of terminals using the set data type,
    # and unresolved expressions using the options data type.
    if type(rule) == options:
        # This is an unresolved rule. Resolve it now.
        all_terminals = set()
        for option in rule:
            logging.debug(f"{prefix} Resolving option {option}")
            resolved = [resolve(rules, r, maxlen, depth=depth+1) for r in option]
            # Now we have a list of resolved rules, each of which is a list of strings/terminals.
            # We need the product of these lists. E.g., suppose:
            # This rule option is 1 2.
            # Resolved rule 1 is ['ab', 'ba']
            # Resolved rule 2 is ['aa', 'bb']
            # 1 2 -> ['ab', 'ba'] x ['aa', 'bb'] -> ['abaa', 'abbb', 'baaa', 'babb']
            logging.debug(f"{prefix} Option {option} resolved -- {len(resolved)} possibilities")
            terminals = [''.join(t) for t in itertools.product(*resolved) if len(t) <= maxlen]
            logging.debug(f"{prefix} Expanded {len(terminals)} terminals")
            all_terminals.update(terminals)

        # Memoize the result: the union of each option's terminals.
        rules[no] = all_terminals

    elif type(rule) == set:
        logging.debug(f"{prefix} Rule #{no} is already resolved. Yay! {len(rule)} possible terminals.")

    return rules[no]

def parse_rule(data):
    return options(s.split(" ") for s in data.split(" | "))

def parse_input(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    rules = {}
    messages = []
    for line in lines:
        if ':' in line:
            r, rest = line.strip().split(': ')
            rules[r] = parse_rule(rest)
        else:
            messages.append(line.strip())
    return rules, messages

def adjust_rules(rules):
    """
    Replaces rules 8 and 11 as described in the problem statement.
    """
    # HACK: To avoid infinite recursion, we unroll the recursive rules a fixed
    # number of times (3). However: A) it is probably not a sufficient number
    # of times to get the correct answer, and B) even at this level, it still
    # results in a too-large explosion of resolved terminals.
    rules['8'] = parse_rule('42 | 42 42 | 42 42 42') #parse_rule('42 | 42 8')
    rules['11'] = parse_rule('42 31 | 42 42 31 31 | 42 42 42 31 31 31') #parse_rule('42 31 | 42 11 31')

def main():
    # Read in the rules.
    rules, messages = parse_input("day19.txt")

    # Resolve rule #0.
    valid_terminals = resolve(rules, '0')
    print(f"Rule #0 has {len(valid_terminals)} possible terminals.")

    # Check each message in our message list.
    print(f"[Part 1] Matching message count = {sum(1 for m in messages if m in valid_terminals)}")

    # Validate part 2 example input.
    ex_rules, ex_messages = parse_input("day19-2-ex.txt")
    ex_valid_terminals = resolve(ex_rules, '0', maxlen=max(len(m) for m in messages))
    print(f"[Part 2] Initial possible terminal count = {len(ex_valid_terminals)}")
    print(f"[Part 2] Initial matching message count = {sum(1 for m in ex_messages if m in ex_valid_terminals)}")

    # Regenerate terminals with adjusted rules in place.
    ex_rules, ex_messages = parse_input("day19-2-ex.txt")
    adjust_rules(ex_rules)
    ex_valid_terminals = resolve(ex_rules, '0', maxlen=max(len(m) for m in ex_messages))
    print(f"[Part 2] Adjusted possible terminal count = {len(ex_valid_terminals)}")
    print(f"[Part 2] Adjusted matching message count = {sum(1 for m in ex_messages if m in ex_valid_terminals)}")

    # Re-resolve rule #0 with adjusted rules in place.
    rules, messages = parse_input("day19.txt")
    adjust_rules(rules)
    valid_terminals = resolve(rules, '0', maxlen=max(len(m) for m in messages))
    print(f"[Part 2] Rule #0 now has {len(valid_terminals)} possible terminals.")

if __name__ == '__main__':
    main()
