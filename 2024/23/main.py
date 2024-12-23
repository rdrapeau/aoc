import networkx as nx

with open('input.txt') as f:
	data = [tuple(x.strip().split('-')) for x in f.readlines()]

G = nx.Graph()
G.add_edges_from(data)

all_cliques = list(nx.enumerate_all_cliques(G))
print(sum(
	1 for c in all_cliques
	if len(c) == 3 and any(x.startswith('t') for x in c)
))

largest = max(all_cliques, key=len)
print(','.join(sorted(largest)))