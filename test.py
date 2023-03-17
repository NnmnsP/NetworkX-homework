def test_mst(): 
    # import the necessary packages
    import random
    import networkx as nx
    import matplotlib.pyplot as plt

    # create a weighted graph
    G = nx.Graph()

    # add nodes
    G.add_nodes_from([1 , 2, 3, 4, 5])

    # generate random weights between 0 and 1 for the edges
    weights = [random.uniform(0, 1) for i in range(6)]

    # add weighted edges to the graph
    G.add_weighted_edges_from([(1, 2, weights[0]), (1, 3, weights[1]), (2, 4, weights[2]), 
                           (3, 4, weights[3]), (3, 5, weights[4]), (4, 5, weights[5])])

    # create a minimum spanning tree\
    T = nx.minimum_spanning_tree(G)

    # assert that the minimum spanning tree is a tree
    assert nx.is_tree(T)

    # assert that the minimum spanning tree has the correct edges
    assert [e for e in T.edges()] == [(1, 2), (1, 3), (3, 5), (4, 5)]