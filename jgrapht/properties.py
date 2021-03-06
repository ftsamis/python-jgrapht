from . import backend


def is_empty_graph(graph):
    """Check whether the graph is empty. An empty graph with 
    n nodes contains n isolates nodes but no edges.

    :param graph: the graph
    :returns: True if the graph is empty, False otherwise.
    """
    res = backend.jgrapht_graph_test_is_empty(graph.handle)
    return res


def is_simple(graph):
    """Check if a graph is simple. A graph is simple if it has 
    no self-loops and multiple edges.

    :param graph: the graph
    :returns: True if simple, False otherwise
    """
    res = backend.jgrapht_graph_test_is_simple(graph.handle)
    return res


def has_selfloops(graph):
    """Check if a graph has self-loops.

    :param graph: the graph
    :returns: True if it has self-loops, False otherwise
    """
    res = backend.jgrapht_graph_test_has_selfloops(graph.handle)
    return res


def has_multipleedges(graph):
    """Check if a graph has multiple-edges.

    :param graph: the graph
    :returns: True if it has multiple-edges, False otherwise
    """
    res = backend.jgrapht_graph_test_has_multipleedges(graph.handle)
    return res


def is_complete(graph):
    """Check if the graph is complete.

    For undirected graphs, each pair of vertices must be connected by a single edge.
    For directed graphs, each pair of vertices must be connected by one pair of edges, one 
    in each direction.

    :param graph: the graph
    :returns: True if the graph is complete, False otherwise
    """
    res = backend.jgrapht_graph_test_is_complete(graph.handle)
    return res


def is_weakly_connected(graph):
    """Test whether a directed graph is weakly connected.
    
    :param graph: the graph. Needs to be directed
    :returns: True if weakly connected, False otherwise
    """
    res = backend.jgrapht_graph_test_is_weakly_connected(graph.handle)
    return res


def is_strongly_connected(graph):
    """Test whether a graph is strongly connected.

    :param graph: the graph
    :returns: True if strongly-connected, False otherwise
    """
    res = backend.jgrapht_graph_test_is_strongly_connected(graph.handle)
    return res


def is_tree(graph):
    """Check if an undirected graph is a tree.

    :param graph: the graph
    :returns: True if the graph is a tree, False otherwise
    """
    res = backend.jgrapht_graph_test_is_tree(graph.handle)
    return res


def is_forest(graph):
    """Check if an undirected graph is a forest.

    :param graph: the graph
    :returns: True if the graph is a forest, False otherwise
    """
    res = backend.jgrapht_graph_test_is_forest(graph.handle)
    return res


def is_overfull(graph):
    r"""Check if the graph is `overfull <https://en.wikipedia.org/wiki/Overfull_graph>`_.

    A graph is overfull if :math:`m > \Delta(G) \lfloor n/2 \rfloor` where :math:`\Delta(G)`
    is the maximum degree in the graph.

    :param graph: the graph
    :returns: True if the graph is ovefull, False otherwise
    """
    res = backend.jgrapht_graph_test_is_overfull(graph.handle)
    return res


def is_split(graph):
    """Test whether an undirected graph is a `split graph <https://en.wikipedia.org/wiki/Split_graph>`_.
    
    :param graph: the graph
    :returns: True if the graph is a split graph, False otherwise
    """
    res = backend.jgrapht_graph_test_is_split(graph.handle)
    return res


def is_bipartite(graph):
    """Check if a graph is bipartite.

    :param graph: the graph
    :returns: True if the graph is bipartite, False otherwise
    """
    res = backend.jgrapht_graph_test_is_bipartite(graph.handle)
    return res


def is_cubic(graph):
    """Check whether a graph is `cubic <https://mathworld.wolfram.com/CubicGraph.html>`_.

    A graph is `cubic <https://mathworld.wolfram.com/CubicGraph.html>`_ if all vertices have
    degree equal to three.

    :param graph: the graph
    :returns: True if the graph is cubic, False otherwise
    """
    res = backend.jgrapht_graph_test_is_cubic(graph.handle)
    return res


def is_eulerian(graph):
    """Check whether a graph is `Eulerian <https://mathworld.wolfram.com/EulerianGraph.html>`_.

    An `Eulerian <https://mathworld.wolfram.com/EulerianGraph.html>`_ graph is a graph containing
    an `Eulerian cycle <https://mathworld.wolfram.com/EulerianCycle.html>`_.

    :param graph: the graph
    :returns: True if the graph is Eulerian, False otherwise
    """
    res = backend.jgrapht_graph_test_is_eulerian(graph.handle)
    return res


def is_chordal(graph):
    """Check where the graph is chordal. 

    :param graph: the graph
    :returns: True if the graph is chordal, False otherwise
    """
    res = backend.jgrapht_graph_test_is_chordal(graph.handle)
    return res


def is_weakly_chordal(graph):
    """Check where the graph is weakly chordal. 

    :param graph: the graph
    :returns: True if the graph is weakly chordal, False otherwise
    """
    res = backend.jgrapht_graph_test_is_weakly_chordal(graph.handle)
    return res


def has_ore(graph):
    """Check whether an undirected graph meets Ore's condition to be Hamiltonian.

    :param graph: The input graph
    :returns: True if the graph meets Ore's condition, False otherwise
    """
    res = backend.jgrapht_graph_test_has_ore(graph.handle)
    return res


def is_trianglefree(graph):
    """Check whether an undirected graph is triangle free.

    :param graph: the graph
    :returns: True if the graph is triangle free, False otherwise
    """
    res = backend.jgrapht_graph_test_is_trianglefree(graph.handle)
    return res


def is_perfect(graph):
    """Check whether a graph is perfect.

    :param graph: the graph
    :returns: True if the graph is perfect, False otherwise
    """
    res = backend.jgrapht_graph_test_is_perfect(graph.handle)
    return res


def is_planar(graph):
    """Check whether a graph is planar.

    :param graph: the graph
    :returns: True if the graph is planar, False otherwise
    """
    res = backend.jgrapht_graph_test_is_planar(graph.handle)
    return res


def is_kuratowski_subdivision(graph):
    """Check whether a graph is a :math:`K_{3,3}` or a :math:`K_5` subdivision.

    :param graph: the graph
    :returns: True if the graph is a :math:`K_{3,3}` or a :math:`K_5` subdivision, False otherwise
    """
    res = backend.jgrapht_graph_test_is_kuratowski_subdivision(graph.handle)
    return res


def is_k33_subdivision(graph):
    """Check whether a graph is a :math:`K_{3,3}` subdivision.

    :param graph: the graph
    :returns: True if the graph is a :math:`K_{3,3}` subdivision, False otherwise
    """
    res = backend.jgrapht_graph_test_is_k33_subdivision(graph.handle)
    return res


def is_k5_subdivision(graph):
    """Check whether a graph is a :math:`K_{5}` subdivision.

    :param graph: the graph
    :returns: True if the graph is a :math:`K_{5}` subdivision, False otherwise
    """
    res = backend.jgrapht_graph_test_is_k5_subdivision(graph.handle)
    return res
