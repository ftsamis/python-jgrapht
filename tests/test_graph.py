import pytest

from jgrapht import create_graph, create_sparse_graph, as_sparse_graph


def assert_same_set(set1, set2):
    assert set1 <= set2 and set2 <= set1


def test_graph_directed_inoutedges():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    assert g.type.directed
    assert g.type.allowing_self_loops
    assert g.type.allowing_multiple_edges
    assert g.type.weighted

    assert g.add_vertex(0)
    v1 = 0
    assert g.add_vertex(1)
    v2 = 1
    assert g.add_vertex(2)
    v3 = 2
    assert g.add_vertex(3)
    v4 = 3
    assert g.add_vertex(4)
    v5 = 4

    vcount = len(g.vertices())
    assert vcount == 5

    assert g.number_of_vertices() == 5

    assert_same_set(set(g.vertices()), set([0, 1, 2, 3, 4]))

    e12 = g.create_edge(v1, v2)
    assert e12 == 0
    assert g.edge_source(e12) == v1
    assert g.edge_target(e12) == v2
    assert g.edge_tuple(e12) == (v1, v2, 1.0)
    e23 = g.create_edge(v2, v3)
    assert g.edge_source(e23) == v2
    assert g.edge_target(e23) == v3
    assert g.edge_tuple(e23) == (v2, v3, 1.0)
    assert e23 == 1
    e14 = g.create_edge(v1, v4)
    assert e14 == 2
    e11 = g.create_edge(v1, v1)
    assert e11 == 3
    e45 = g.create_edge(v4, v5)
    assert e45 == 4
    e51_1 = g.create_edge(v5, v1)
    assert e51_1 == 5
    e51_2 = g.create_edge(v5, v1)
    assert e51_2 == 6

    assert len(g.edges()) == 7

    assert g.contains_edge_between(v1, v4)
    assert not g.contains_edge_between(v1, v5)

    assert_same_set(set(g.edges_of(v1)), set([e12, e14, e11, e51_1, e51_2]))
    assert_same_set(set(g.outedges_of(v1)), set([e12, e14, e11]))
    assert_same_set(set(g.inedges_of(v1)), set([e51_1, e51_2, e11]))
    assert g.degree_of(v1) == 6 # self-loops count twice!
    assert g.outdegree_of(v1) == 3
    assert g.indegree_of(v1) == 3

    assert_same_set(set(g.edges_of(v2)), set([e12, e23]))
    assert_same_set(set(g.outedges_of(v2)), set([e23]))
    assert_same_set(set(g.inedges_of(v2)), set([e12]))
    assert g.degree_of(v2) == 2
    assert g.outdegree_of(v2) == 1
    assert g.indegree_of(v2) == 1

    assert_same_set(set(g.edges_of(v3)), set([e23]))
    assert_same_set(set(g.outedges_of(v3)), set())
    assert_same_set(set(g.inedges_of(v3)), set([e23]))
    assert g.degree_of(v3) == 1
    assert g.outdegree_of(v3) == 0
    assert g.indegree_of(v3) == 1

    assert_same_set(set(g.edges_of(v4)), set([e45, e14]))
    assert_same_set(set(g.outedges_of(v4)), set([e45]))
    assert_same_set(set(g.inedges_of(v4)), set([e14]))
    assert g.degree_of(v4) == 2
    assert g.outdegree_of(v4) == 1
    assert g.indegree_of(v4) == 1

    assert_same_set(set(g.edges_of(v5)), set([e45, e51_1, e51_2]))
    assert_same_set(set(g.outedges_of(v5)), set([e51_1, e51_2]))
    assert_same_set(set(g.inedges_of(v5)), set([e45]))
    assert g.degree_of(v5) == 3
    assert g.outdegree_of(v5) == 2
    assert g.indegree_of(v5) == 1    

    assert_same_set(set(g.edges()), set([0, 1, 2, 3, 4, 5, 6]))


def test_graph_undirected_inoutedges():

    g = create_graph(directed=False, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    assert not g.type.directed
    assert g.type.allowing_self_loops
    assert g.type.allowing_multiple_edges
    assert g.type.weighted

    assert g.add_vertex(0)
    v1 = 0
    assert g.add_vertex(1)
    v2 = 1
    assert g.add_vertex(2)
    v3 = 2
    assert g.add_vertex(3)
    v4 = 3
    assert g.add_vertex(4)
    v5 = 4

    vcount = len(g.vertices())
    assert vcount == 5

    assert_same_set(set(g.vertices()), set([0, 1, 2, 3, 4]))

    e12 = g.create_edge(v1, v2)
    assert e12 == 0
    assert g.edge_source(e12) == v1
    assert g.edge_target(e12) == v2
    assert g.edge_tuple(e12) == (v1, v2, 1.0)
    e23 = g.create_edge(v2, v3)
    assert g.edge_source(e23) == v2
    assert g.edge_target(e23) == v3
    assert g.edge_tuple(e23) == (v2, v3, 1.0)
    assert e23 == 1
    e14 = g.create_edge(v1, v4)
    assert e14 == 2
    e11 = g.create_edge(v1, v1)
    assert e11 == 3
    e45 = g.create_edge(v4, v5)
    assert e45 == 4
    e51_1 = g.create_edge(v5, v1)
    assert e51_1 == 5
    e51_2 = g.create_edge(v5, v1)
    assert e51_2 == 6

    assert len(g.edges()) == 7

    assert g.contains_edge_between(v1, v4)
    assert g.contains_edge_between(v1, v5)

    assert_same_set(set(g.edges_between(v1, v5)), set([e51_1, e51_2]))

    assert_same_set(set(g.edges_of(v1)), set([e12, e14, e11, e51_1, e51_2]))
    assert_same_set(set(g.outedges_of(v1)), set([e12, e14, e11, e51_1, e51_2]))
    assert_same_set(set(g.inedges_of(v1)), set([e12, e14, e11, e51_1, e51_2]))
    assert g.degree_of(v1) == 6 # self-loops count twice!
    assert g.outdegree_of(v1) == 6
    assert g.indegree_of(v1) == 6

    assert_same_set(set(g.edges_of(v2)), set([e12, e23]))
    assert_same_set(set(g.outedges_of(v2)), set([e12, e23]))
    assert_same_set(set(g.inedges_of(v2)), set([e12, e23]))
    assert g.degree_of(v2) == 2
    assert g.outdegree_of(v2) == 2
    assert g.indegree_of(v2) == 2

    assert_same_set(set(g.edges_of(v3)), set([e23]))
    assert_same_set(set(g.outedges_of(v3)), set([e23]))
    assert_same_set(set(g.inedges_of(v3)), set([e23]))
    assert g.degree_of(v3) == 1
    assert g.outdegree_of(v3) == 1
    assert g.indegree_of(v3) == 1

    assert_same_set(set(g.edges_of(v4)), set([e45, e14]))
    assert_same_set(set(g.outedges_of(v4)), set([e45, e14]))
    assert_same_set(set(g.inedges_of(v4)), set([e45, e14]))
    assert g.degree_of(v4) == 2
    assert g.outdegree_of(v4) == 2
    assert g.indegree_of(v4) == 2

    assert_same_set(set(g.edges_of(v5)), set([e45, e51_1, e51_2]))
    assert_same_set(set(g.outedges_of(v5)), set([e45, e51_1, e51_2]))
    assert_same_set(set(g.inedges_of(v5)), set([e45, e51_1, e51_2]))
    assert g.degree_of(v5) == 3
    assert g.outdegree_of(v5) == 3
    assert g.indegree_of(v5) == 3  

    assert_same_set(set(g.edges()), set([0, 1, 2, 3, 4, 5, 6]))


def test_graph_no_allow_self_loops():

    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=True, weighted=True)

    assert g.type.directed
    assert not g.type.allowing_self_loops
    assert g.type.allowing_multiple_edges
    assert g.type.weighted

    v1 = 0
    assert g.add_vertex(v1)

    with pytest.raises(ValueError):
        g.create_edge(v1, v1)


def test_graph_no_allow_multiple_edges():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=False, weighted=True)

    assert g.type.directed
    assert g.type.allowing_self_loops
    assert not g.type.allowing_multiple_edges
    assert g.type.weighted

    v1 = 0
    assert g.add_vertex(v1)
    v2 = 1
    assert g.add_vertex(v2)

    g.create_edge(v1, v2)
    with pytest.raises(ValueError):
        g.create_edge(v1, v2)


def test_graph_no_weights():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=False, weighted=False)

    assert g.type.directed
    assert g.type.allowing_self_loops
    assert not g.type.allowing_multiple_edges
    assert not g.type.weighted

    v1 = 0
    assert g.add_vertex(v1)
    v2 = 1
    assert g.add_vertex(v2)

    e12 = g.create_edge(v1, v2)

    assert g.get_edge_weight(e12) == 1.0

    with pytest.raises(ValueError):
        g.set_edge_weight(e12, 10.0)


def test_graph_create_edge_with_weight():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=False, weighted=True)

    v1 = 0
    assert g.add_vertex(v1)
    v2 = 1
    assert g.add_vertex(v2)

    e12 = g.create_edge(v1, v2, weight=55.0)
    assert g.get_edge_weight(e12) == 55.0


def test_graph_add_edge():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    g.add_vertices_from([1,2])

    assert g.create_edge(1,2) == 0
    assert g.create_edge(1,2) == 1
    assert g.create_edge(1,2) == 2
    assert g.create_edge(1,2) == 3

    assert g.add_edge(1, 2, 5)
    assert g.contains_edge(5)

    assert g.create_edge(1,2) == 4
    assert g.create_edge(1,2) == 6

    assert not g.add_edge(1, 2, 5)


def test_graph_add_vertex():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    assert g.create_vertex() == 0
    assert g.create_vertex() == 1
    g.add_vertices_from([2, 3, 4])
    assert len(g.vertices()) == 5

    assert g.create_vertex() == 5
    assert not g.add_vertex(5)

    assert len(g.vertices()) == 6


def test_graph_sparse():

    edgelist = [(0,1), (0,2), (0,3), (1,3), (2,3), (2,4), (2,5), (0,4), (2, 6)]
    g = create_sparse_graph(7, edgelist, weighted=False)

    assert g.type.directed
    assert not g.type.weighted

    assert g.vertices() == set([0, 1, 2, 3, 4, 5, 6])

    edgelist2 = []
    for e in g.edges(): 
        u, v, w = g.edge_tuple(e)
        edgelist2.append((u,v))
    assert edgelist2 == edgelist

    # sparse graphs cannot be modified
    with pytest.raises(ValueError):
        g.create_edge(0,5)


def test_graph_sparse_weighted():

    edgelist = [(0,1,5), (0,2,2), (0,3,3), (1,3,1), (2,3,7.7), (2,4,3.3), (2,5,13.0), (0,4,9.999), (2,6,3.0)]
    g = create_sparse_graph(7, edgelist, directed=False)

    assert not g.type.directed
    assert g.type.weighted

    assert g.vertices() == set([0, 1, 2, 3, 4, 5, 6])

    edgelist2 = []
    for e in g.edges(): 
        edgelist2.append(g.edge_tuple(e))
    assert edgelist2 == edgelist

    # sparse graphs cannot be modified
    with pytest.raises(ValueError):
        g.create_edge(0,5)


def test_graph_copy_to_sparse():

    g = create_graph(directed=False, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    assert not g.type.directed
    assert g.type.allowing_self_loops
    assert g.type.allowing_multiple_edges
    assert g.type.weighted

    assert g.add_vertex(0)
    v1 = 0
    assert g.add_vertex(1)
    v2 = 1
    assert g.add_vertex(2)
    v3 = 2
    assert g.add_vertex(3)
    v4 = 3
    assert g.add_vertex(4)
    v5 = 4

    assert g.vertices(), set([0, 1, 2, 3, 4])

    e12 = g.create_edge(v1, v2)
    e23 = g.create_edge(v2, v3)
    e14 = g.create_edge(v1, v4)
    e11 = g.create_edge(v1, v1)
    e45 = g.create_edge(v4, v5)
    e51_1 = g.create_edge(v5, v1)
    e51_2 = g.create_edge(v5, v1)

    assert len(g.edges()) == 7

    gs = as_sparse_graph(g)

    assert gs.vertices(), set([0, 1, 2, 3, 4])
    assert len(gs.edges()) == 7


def test_graph_copy_to_sparse():

    g = create_graph(directed=True, allowing_self_loops=True, allowing_multiple_edges=True, weighted=True)

    assert g.type.directed
    assert g.type.allowing_self_loops
    assert g.type.allowing_multiple_edges
    assert g.type.weighted

    assert g.add_vertex(0)
    assert g.add_vertex(5)
    assert g.add_vertex(10)

    g.create_edge(0, 10)
    g.create_edge(0, 5)
    g.create_edge(10, 5)

    assert len(g.edges()) == 3

    gs = as_sparse_graph(g)

    assert gs.vertices(), set(range(0, 11))
    assert len(gs.edges()) == 3
    assert gs.type.weighted
    assert gs.type.directed
