"""
You run a store with N registers in a row. You have M cashiers (M <= N).
Your job is to assign each cashier to a register, such that all cashiers
get along. The catch is that some cashiers cannot be stationed at
adjacent registers, because they will fight or gossip at the expense of
good customer service.

Notes:
    * This problem can be represented as Hamiltonian path of undirected graph.
    * Therefore, in general, it is NP-complete.
    * However, if N > M, the problem changes: for each extra register we have,
      we can afford one bisection of the graph.
    * Could look at networkx package to make implementation simpler.
"""
