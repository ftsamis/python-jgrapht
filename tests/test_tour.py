import pytest

from jgrapht import create_graph
from jgrapht.generators import complete_graph
import jgrapht.algorithms.tour as tour

from random import Random

def build_graph():
    g = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)
    complete_graph(g, 8)

    rng = Random(17)

    for e in g.edges():
        g.set_edge_weight(e, rng.randint(0,10))

    return g

def test_random_tsp():
    g = build_graph()
    path = tour.tsp_random(g, 17)
    assert path.weight == 43.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 2


def test_greedy_heuristic():
    g = build_graph()
    path = tour.tsp_greedy_heuristic(g)
    assert path.weight == 27.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 0


def test_tour_tsp_nearest_insertion_heuristic():
    g = build_graph()
    path = tour.tsp_nearest_insertion_heuristic(g)
    assert path.weight == 30.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 1


def test_tour_tsp_nearest_neighbor_heuristic():
    g = build_graph()
    path = tour.tsp_nearest_neighbor_heuristic(g, seed=17)
    assert path.weight == 33.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 5


def test_metric_tsp_christophides():
    # We only test the API here, not enforcing metric instance
    g = build_graph()
    path = tour.metric_tsp_christofides(g)
    assert path.weight == 28.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 7


def test_metric_tsp_two_approx():
    # We only test the API here, not enforcing metric instance
    g = build_graph()
    path = tour.metric_tsp_two_approx(g)
    assert path.weight == 28.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 7


def test_tsp_held_karp():
    g = build_graph()
    path = tour.tsp_held_karp(g)
    assert path.weight == 27.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 0


def test_hamiltonian_palmer():
    g = build_graph()
    path = tour.hamiltonian_palmer(g)
    assert path.weight == 8.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 0


def test_tsp_two_opt_heuristic():
    g = build_graph()
    path = tour.tsp_two_opt_heuristic(g, seed=17)
    assert path.weight == 27.0
    assert path.start_vertex == path.end_vertex
    assert path.start_vertex == 2


def test_tsp_two_opt_improve():
    g = build_graph()
    
    path1 = tour.tsp_nearest_insertion_heuristic(g)
    assert path1.weight == 30.0
    assert path1.start_vertex == path1.end_vertex
    assert path1.start_vertex == 1    

    path2 = tour.tsp_two_opt_heuristic_improve(path1, seed=17)
    assert path2.weight == 27.0
    assert path2.start_vertex == path2.end_vertex
    assert path2.start_vertex == 1


