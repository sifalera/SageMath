import networkx as nx

G = nx.binomial_graph(10, 0.5, seed=None, directed=False)

nx.draw(G, with_labels=True)