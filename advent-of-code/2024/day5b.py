from graphlib import TopologicalSorter

with open("day5.txt") as f:
    lines = [line.strip() for line in f.readlines()]

rules = [line.split("|") for line in lines if "|" in line]
printouts = [line.split(",") for line in lines if "," in line]

def fixup(printout):
    # Build the graph.
    graph = {item: set() for item in printout}
    for rule in rules:
        before = rule[0]
        after = rule[1]
        if before not in graph or after not in graph:
            # irrelevant rule
            continue
        graph[after].add(before)
    return list(TopologicalSorter(graph).static_order())

middles = []
for printout in printouts:
    fixed = fixup(printout)
    if fixed != printout:
        print(f"{printout} -> {fixed}")
        middles.append(int(fixed[len(fixed) // 2]))

print(sum(middles))
