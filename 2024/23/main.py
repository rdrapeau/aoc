import networkx as nx
from itertools import permutations

with open('input.txt') as f:
	data = [tuple(x.strip().split('-')) for x in f.readlines()]

all_edges = set(data + [tuple([x[1], x[0]]) for x in data])

G = nx.Graph()
G.add_edges_from(all_edges)

print(sum(
	1 for c in nx.enumerate_all_cliques(G)
	if len(c) == 3 and any(x.startswith('t') for x in c)
))

largest = max(nx.find_cliques(G), key=len)
print(','.join(sorted(largest)))