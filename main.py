import networkx as nx
import matplotlib.pyplot as plt

def test_shortest_path():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=3)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'D', weight=4)
    G.add_edge('C', 'D', weight=1)
    assert nx.shortest_path(G, 'A', 'D', weight='weight') == ['A', 'C', 'D']

G = nx.erdos_renyi_graph(10, 0.3)
for (u, v, w) in G.edges(data=True):
    w['weight'] = round(random.uniform(0.1, 1.0), 1)
    
pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw_networkx_labels(G, pos)
nx.draw(G, pos)
plt.savefig("graph.png")

start = list(G.nodes())[0]
end = list(G.nodes())[-1]
path = nx.shortest_path(G, start, end, weight='weight')
print(path)

path_edges = list(zip(path, path[1:]))
edge_colors = ['r' if edge in path_edges else 'black' for edge in G.edges()]
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw_networkx_labels(G, pos)
nx.draw(G, pos, edge_color=edge_colors)
plt.savefig("shortest_path.png")

