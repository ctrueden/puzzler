import networkx as nx

matrix = []
with open("p107_network.txt", "r") as file_in:
    for line in file_in:
        tokens = line.strip().split(",")
        row = [int(x) if x != "-" else -1 for x in tokens]
        matrix.append(row)

G = nx.cycle_graph(40)
for i in range(40):
    for j in range(i + 1, 40):
        if matrix[i][j] >= 0:
            G.add_edge(i, j, weight=matrix[i][j])

M = nx.minimum_spanning_tree(G)

default_weight = 1000000
orig_sum = sum(e[2].get('weight', default_weight) for e in G.edges(data=True))
print(orig_sum)
print(G.edges(data=True))

min_sum = sum(e[2].get('weight', default_weight) for e in M.edges(data=True))
print(min_sum)
print(M.edges(data=True))

print(orig_sum - min_sum)
