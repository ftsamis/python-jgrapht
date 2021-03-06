import pytest

from jgrapht import create_graph
import jgrapht.algorithms.flow as flow

def _do_run_cut(algo):
    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    e01 = g.create_edge(0, 1, weight=20)
    e02 = g.create_edge(0, 2, weight=10)
    g.create_edge(1, 2, weight=30)
    g.create_edge(1, 3, weight=10)
    g.create_edge(2, 3, weight=20)

    cut = algo(g, 0, 3)

    assert cut.capacity == 30.0
    assert cut.edges == set([e01, e02])
    assert cut.source_partition == set([0])
    assert cut.target_partition == set([1,2,3])

def _do_run_both(algo):
    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    e01 = g.create_edge(0, 1, weight=20)
    e02 = g.create_edge(0, 2, weight=10)
    e12 = g.create_edge(1, 2, weight=30)
    e13 = g.create_edge(1, 3, weight=10)
    e23 = g.create_edge(2, 3, weight=20)

    f, cut = algo(g, 0, 3)

    assert f.source == 0
    assert f.sink == 3
    assert f.value == 30.0
    assert f[e01] == 20.0
    assert f[e02] == 10.0
    assert f[e12] == 10.0
    assert f[e13] == 10.0
    assert f[e23] == 20.0

    assert cut.capacity == 30.0
    assert cut.edges == set([e01, e02])
    assert cut.source_partition == set([0])
    assert cut.target_partition == set([1,2,3])

def _do_run_flow(algo):
    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    e01 = g.create_edge(0, 1, weight=20)
    e02 = g.create_edge(0, 2, weight=10)
    e12 = g.create_edge(1, 2, weight=30)
    e13 = g.create_edge(1, 3, weight=10)
    e23 = g.create_edge(2, 3, weight=20)

    f = algo(g, 0, 3)

    assert f.source == 0
    assert f.sink == 3
    assert f.value == 30.0
    assert f[e01] == 20.0
    assert f[e02] == 10.0
    assert f[e12] == 10.0
    assert f[e13] == 10.0
    assert f[e23] == 20.0


def test_dinic():
    _do_run_both(flow.dinic)

def test_push_relabel():
    _do_run_both(flow.push_relabel)

def test_edmonds_karp():
    _do_run_both(flow.edmonds_karp)

def test_min_st_cut():
    _do_run_cut(flow.min_st_cut)

def test_max_st_flow():
    _do_run_flow(flow.max_st_flow)    