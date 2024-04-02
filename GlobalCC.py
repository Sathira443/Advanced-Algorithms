import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from([(1, 2), (1, 5), (4, 6), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)])
print(nx.transitivity(g))

subax1 = plt.subplot(121)
nx.draw(g, with_labels=True, font_weight='bold')