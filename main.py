# import necessary libraries
import networkx as nx
import random
import matplotlib.pyplot as plt

# create an empty graph
G = nx.Graph()

# add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# generate random weights between 0 and 1 for the edges
weights = [random.uniform(0, 1) for i in range(6)]

# add weighted edges to the graph
G.add_weighted_edges_from([(1, 2, weights[0]), (1, 3, weights[1]), (2, 4, weights[2]), 
                           (3, 4, weights[3]), (3, 5, weights[4]), (4, 5, weights[5])])

# get the positions of the nodes using the spring layout algorithm
pos = nx.spring_layout(G)

# draw the graph with labels and edge weights
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# save the graph as an image and clear the figure
plt.savefig("weighted_graph.png")
plt.clf()

# find the minimum spanning tree of the graph
T = nx.minimum_spanning_tree(G)

# draw the minimum spanning tree with red nodes and edges, and show edge weights in red font
nx.draw(T, pos, with_labels=True, node_color='red', edge_color='red')
nx.draw_networkx_edge_labels(T, pos, edge_labels=nx.get_edge_attributes(T, 'weight'), font_color='red')

# save the minimum spanning tree as an image
plt.savefig("MST.png")
