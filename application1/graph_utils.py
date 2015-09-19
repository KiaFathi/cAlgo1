"""
Project 1 Programming Assignment
"""

EX_GRAPH0 = {
    0: set([1, 2]),
    1: set([]),
    2: set([])
}

EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}

EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 4, 5, 6, 7, 3])
}

def make_complete_graph(num_nodes):
    """
    Makes a complete directed graph as a dictonary.

    Returns a dictionary
    """
    new_graph = dict()
    if num_nodes < 1:
        return new_graph
    for idx in range(0, num_nodes):
        new_graph[idx] = set()
        for edge_idx in range(0, num_nodes):
            if idx != edge_idx:
                new_graph[idx].add(edge_idx)

    return new_graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph, digraph, and computes the in-degrees for the nodes
    in the graph.

    Returns a dictionary with the same set of keys as digraph whose values
    are the number of edges whose head matches a particular node
    """

    in_degrees = dict()
    for node in digraph:
        in_degrees[node] = 0
    for node in digraph:
        for edge in digraph[node]:
            in_degrees[edge] += 1
    return in_degrees


def in_degree_distribution(digraph):
    """
    Takes a directed graph, digraph, and returns the unnormalized distribution
    of the in-degrees of the graph.

    Returns a dictionary whose keys correspond to in-degrees of nodes in
    the graph. The value associated with each particular in-degree is the
    number of nodes with that in-degree. In-degrees with no corresponding nodes
    in the graph are not included in the dictionary.
    """
    in_degrees = compute_in_degrees(digraph)
    distribution = dict()
    for node in in_degrees:
        if distribution.get(in_degrees[node], False):
            distribution[in_degrees[node]] += 1
        else:
            distribution[in_degrees[node]] = 1

    return distribution

def normalized_in_degree_distribution(digraph):
    """
    Takes a directed graph, digraph, and calculate the normalized distribution
    of the in-degrees of the graph.

    Returns a dictionary whoe keys correspond to the in-degrees of nodes in the
    graph. The value associated with each particular in-degree is the number of
    nodes with that in-degree normalized by the total number of in-degrees
    """
    distribution = in_degree_distribution(digraph)
    num_in_degrees = 0
    for key in distribution:
        num_in_degrees += distribution[key]

    return {k: float(v) / num_in_degrees for k, v in distribution.iteritems()}

