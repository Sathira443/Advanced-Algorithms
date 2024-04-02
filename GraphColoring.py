import networkx as nx

# Assuming 'G' is your graph
G = nx.Graph()

# Add edges to 'G' according to your graph
G.add_edge('A', 'B')
G.add_edge('A', 'E')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'D')
G.add_edge('C', 'E')
G.add_edge('D', 'E')

# Calculate the global clustering coefficient
coeff = nx.transitivity(G)

print(f"The global clustering coefficient of the graph is {coeff}")

# triangles = nx.triangles(G)
# print(f"Triangles: {triangles}")
#
# triads = nx.all_triads(G)
# print(f"Triads: {triads}")
