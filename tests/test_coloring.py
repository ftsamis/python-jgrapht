import pytest

from jgrapht import create_graph
import jgrapht.algorithms.coloring as coloring

def test_coloring():
    g = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    for i in range(0, 10):
        g.add_vertex(i)

    vcount = len(g.vertices())
    assert vcount == 10

    g.create_edge(0, 1)
    g.create_edge(0, 2)
    g.create_edge(0, 3)
    g.create_edge(0, 4)
    g.create_edge(0, 5)
    g.create_edge(0, 6)
    g.create_edge(0, 7)
    g.create_edge(0, 8)
    g.create_edge(0, 9)

    g.create_edge(1, 2)
    g.create_edge(2, 3)
    g.create_edge(3, 4)
    g.create_edge(4, 5)
    g.create_edge(5, 6)
    g.create_edge(6, 7)
    g.create_edge(7, 8)
    g.create_edge(8, 9)
    g.create_edge(9, 1)

    assert len(g.edges()) == 18

    color_count, color_map = coloring.greedy_smallestnotusedcolor(g)
    assert color_count == 4
    assert all([a == b for a,b in zip([color_map[v] for v in g.vertices()], [0, 1, 2, 1, 2, 1, 2, 1, 2, 3])]) 
    assert all([color_map[u]!=color_map[v] for u, v in zip([g.edge_source(e) for e in g.edges()], [g.edge_target(e) for e in g.edges()])])
    

    color_count, color_map = coloring.greedy_random(g, seed=17)
    assert color_count == 4
    assert all([a == b for a,b in zip([color_map[v] for v in g.vertices()], [1, 2, 0, 2, 0, 2, 3, 0, 2, 0])])
    assert all([color_map[u]!=color_map[v] for u, v in zip([g.edge_source(e) for e in g.edges()], [g.edge_target(e) for e in g.edges()])]) 

    color_count, color_map = coloring.greedy_dsatur(g)
    assert color_count == 4
    assert all([a == b for a,b in zip([color_map[v] for v in g.vertices()], [0, 1, 2, 1, 2, 1, 3, 2, 1, 2])])
    assert all([color_map[u]!=color_map[v] for u, v in zip([g.edge_source(e) for e in g.edges()], [g.edge_target(e) for e in g.edges()])])     

    color_count, color_map = coloring.backtracking_brown(g)
    assert color_count == 4
    assert all([a == b for a,b in zip([color_map[v] for v in g.vertices()], [1, 2, 3, 2, 3, 2, 3, 2, 3, 4])])    
    assert all([color_map[u]!=color_map[v] for u, v in zip([g.edge_source(e) for e in g.edges()], [g.edge_target(e) for e in g.edges()])])         

    color_count, color_map = coloring.color_refinement(g)
    assert color_count == 10
