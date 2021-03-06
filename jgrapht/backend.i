%module backend

%{
#define SWIG_FILE_WITH_INIT
#include "backend.h"
%}


%include <typemaps.i>

// custom typemap to append void** types to the result
%typemap(in,numinputs=0,noblock=1) void **OUTPUT ($*1_ltype temp) {
    $1 = &temp;
}

%typemap(argout,noblock=1) void **OUTPUT {
    %append_output(SWIG_NewPointerObj(*$1, $*1_descriptor, SWIG_POINTER_NOSHADOW | %newpointer_flags));
}

%typemap(in,numinputs=0,noblock=1) char **OUTPUT ($*1_ltype temp) {
    $1 = &temp;
}

%typemap(argout,noblock=1) char **OUTPUT {
    %append_output(SWIG_FromCharPtr(($*1_ltype)*$1));
}

%typemap(in) void *LONG_TO_FUNCTION_POINTER { 
    $1 = PyLong_AsVoidPtr($input);    
}

enum status_t { 
    STATUS_SUCCESS = 0,
    STATUS_ERROR,
    STATUS_ILLEGAL_ARGUMENT,
    STATUS_UNSUPPORTED_OPERATION,
    STATUS_INDEX_OUT_OF_BOUNDS,
    STATUS_NO_SUCH_ELEMENT,
    STATUS_NULL_POINTER,
    STATUS_CLASS_CAST,
    STATUS_IO_ERROR,
    STATUS_EXPORT_ERROR,
    STATUS_IMPORT_ERROR,
    STATUS_NEGATIVE_CYCLE_DETECTED,
};

enum dimacs_format_t {
    DIMACS_FORMAT_SHORTEST_PATH = 0,
    DIMACS_FORMAT_MAX_CLIQUE,
    DIMACS_FORMAT_COLORING,
};

enum csv_format_t {
    CSV_FORMAT_EDGE_LIST = 0,
    CSV_FORMAT_ADJACENCY_LIST,
    CSV_FORMAT_MATRIX,
};

// library init

void jgrapht_isolate_create();

void jgrapht_isolate_destroy();

int jgrapht_isolate_is_attached();

// error

void jgrapht_error_clear_errno();

int jgrapht_error_get_errno();

char *jgrapht_error_get_errno_msg();

void jgrapht_error_print_stack_trace();

// vm

void jgrapht_vmLocatorSymbol();

// exception handling
// grab result from C and throw python exception

%{
int raise_exception_on_error(int result) { 
    if (result != STATUS_SUCCESS) {
        switch(result) {
        case STATUS_ILLEGAL_ARGUMENT:
            PyErr_SetString(PyExc_ValueError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_UNSUPPORTED_OPERATION:
            PyErr_SetString(PyExc_ValueError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_INDEX_OUT_OF_BOUNDS:
            PyErr_SetString(PyExc_IndexError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_NO_SUCH_ELEMENT:
            PyErr_SetString(PyExc_KeyError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_NULL_POINTER:
            PyErr_SetString(PyExc_ValueError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_CLASS_CAST:
            PyErr_SetString(PyExc_TypeError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_IO_ERROR:
        case STATUS_EXPORT_ERROR:
        case STATUS_IMPORT_ERROR:
            PyErr_SetString(PyExc_IOError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_NEGATIVE_CYCLE_DETECTED:
            PyErr_SetString(PyExc_ValueError, jgrapht_error_get_errno_msg());
            break;
        case STATUS_ERROR:
        default:
            PyErr_SetString(PyExc_RuntimeError, jgrapht_error_get_errno_msg());
            break;
        }
        jgrapht_error_clear_errno();
        return 1;
    }
    return 0;
}
%}

%exception { 
    $action
    if (raise_exception_on_error(result)) { 
        SWIG_fail;
    }
}

// ignore the integer return code
// we already handled this using the exception 
%typemap(out) int  "$result = SWIG_Py_Void();";


// Put some init code in python
%pythonbegin %{
# The Python-JGraphT library
%}

// attribute store 

int jgrapht_attributes_store_create(void** OUTPUT);

int jgrapht_attributes_store_put_boolean_attribute(void *, int, char*, int);

int jgrapht_attributes_store_put_int_attribute(void *, int, char*, int);

int jgrapht_attributes_store_put_long_attribute(void *, long long int, char*, int);

int jgrapht_attributes_store_put_double_attribute(void *, int, char*, double);

int jgrapht_attributes_store_put_string_attribute(void *, int, char*, char*);

int jgrapht_attributes_store_remove_attribute(void *, int, char*);

int jgrapht_attributes_registry_create(void** OUTPUT);

int jgrapht_attributes_registry_register_attribute(void *, char*, char*, char*, char*);

int jgrapht_attributes_registry_unregister_attribute(void *, char*, char*, char*, char*);

// clique

int jgrapht_clique_exec_bron_kerbosch(void *, long long int, void** OUTPUT);

int jgrapht_clique_exec_bron_kerbosch_pivot(void *, long long int, void** OUTPUT);

int jgrapht_clique_exec_bron_kerbosch_pivot_degeneracy_ordering(void *, long long int, void** OUTPUT);

// clustering

int jgrapht_clustering_exec_k_spanning_tree(void *, int, void** OUTPUT);

int jgrapht_clustering_exec_label_propagation(void *, int, long long int, void** OUTPUT);

int jgrapht_clustering_get_number_clusters(void *, int* OUTPUT);

int jgrapht_clustering_ith_cluster_vit(void *, int, void** OUTPUT);

// coloring

int jgrapht_coloring_exec_greedy(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_greedy_smallestdegreelast(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_backtracking_brown(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_greedy_largestdegreefirst(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_greedy_random(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_greedy_random_with_seed(void *, long long int, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_greedy_dsatur(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_coloring_exec_color_refinement(void *, int* OUTPUT, void** OUTPUT);

// connectivity

int jgrapht_connectivity_strong_exec_kosaraju(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_connectivity_strong_exec_gabow(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_connectivity_weak_exec_bfs(void *, int* OUTPUT, void** OUTPUT);

// cut

int jgrapht_cut_exec_stoer_wagner(void *, double* OUTPUT, void** OUTPUT);

// cycles

int jgrapht_cycles_eulerian_exec_hierholzer(void *, int* OUTPUT, void** OUTPUT);

int jgrapht_cycles_chinese_postman_exec_edmonds_johnson(void *, void** OUTPUT);

int jgrapht_cycles_simple_enumeration_exec_tarjan(void *, void** OUTPUT);

int jgrapht_cycles_simple_enumeration_exec_tiernan(void *, void** OUTPUT);

int jgrapht_cycles_simple_enumeration_exec_szwarcfiter_lauer(void *, void** OUTPUT);

int jgrapht_cycles_simple_enumeration_exec_johnson(void *, void** OUTPUT);

int jgrapht_cycles_simple_enumeration_exec_hawick_james(void *, void** OUTPUT);

int jgrapht_cycles_fundamental_basis_exec_queue_bfs(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_cycles_fundamental_basis_exec_stack_bfs(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_cycles_fundamental_basis_exec_paton(void *, double* OUTPUT, void** OUTPUT);


// exporter

int jgrapht_export_file_dimacs(void *, char*, dimacs_format_t, int);

int jgrapht_export_string_dimacs(void *, dimacs_format_t, int, void** OUTPUT);

int jgrapht_export_file_gml(void *, char*, int, void *, void *);

int jgrapht_export_string_gml(void *, int, void *, void *, void **OUTPUT);

int jgrapht_export_file_json(void *, char*, void *, void *);

int jgrapht_export_string_json(void *, void *, void *, void **OUTPUT);

int jgrapht_export_file_lemon(void *, char*, int, int);

int jgrapht_export_string_lemon(void *, int, int, void **OUTPUT);

int jgrapht_export_file_csv(void *, char*, csv_format_t, int, int, int);

int jgrapht_export_string_csv(void *, csv_format_t, int, int, int, void **OUTPUT);

int jgrapht_export_file_gexf(void *, char*, void *, void *, void *, int, int, int, int);

int jgrapht_export_string_gexf(void *, void *, void *, void *, int, int, int, int, void **OUTPUT);

int jgrapht_export_file_dot(void *, char*, void *, void *);

int jgrapht_export_string_dot(void *, void *, void *, void **OUTPUT);

int jgrapht_export_file_graph6(void *, char*);

int jgrapht_export_string_graph6(void *, void **OUTPUT);

int jgrapht_export_file_sparse6(void *, char*);

int jgrapht_export_string_sparse6(void *, void** OUTPUT);

int jgrapht_export_file_graphml(void *, char*, void *, void *, void *, int, int, int);

int jgrapht_export_string_graphml(void *, void *, void *, void *, int, int, int, void** OUTPUT);

// flow 

int jgrapht_maxflow_exec_push_relabel(void *, int, int, double* OUTPUT, void** OUTPUT, void** OUTPUT);

int jgrapht_maxflow_exec_dinic(void *, int, int, double* OUTPUT, void** OUTPUT, void** OUTPUT);

int jgrapht_maxflow_exec_edmonds_karp(void *, int, int, double* OUTPUT, void** OUTPUT, void** OUTPUT);

int jgrapht_mincostflow_exec_capacity_scaling(void *, void *, void *, void *, int, double* OUTPUT, void** OUTPUT, void** OUTPUT);

// generate

int jgrapht_generate_barabasi_albert(void *, int, int, int, long long int);

int jgrapht_generate_barabasi_albert_forest(void *, int, int, long long int);

int jgrapht_generate_complete(void *, int);

int jgrapht_generate_bipartite_complete(void *, int, int);

int jgrapht_generate_empty(void *, int);

int jgrapht_generate_gnm_random(void *, int, int, int, int, long long int);

int jgrapht_generate_gnp_random(void *, int, double, int, long long int);

int jgrapht_generate_ring(void *, int);

int jgrapht_generate_scalefree(void *, int, long long int);

int jgrapht_generate_watts_strogatz(void *, int, int, double, int, long long int);

int jgrapht_generate_kleinberg_smallworld(void *, int, int, int, int, long long int);

// graph

int jgrapht_graph_create(int, int, int, int, void **OUTPUT);

int jgrapht_graph_sparse_create(int, int, int, void *, void** OUTPUT);

int jgrapht_graph_vertices_count(void *, int* OUTPUT);

int jgrapht_graph_edges_count(void *, int* OUTPUT);

int jgrapht_graph_add_vertex(void *, int* OUTPUT);

int jgrapht_graph_add_given_vertex(void *, int, int *OUTPUT);

int jgrapht_graph_remove_vertex(void *, int, int* OUTPUT);

int jgrapht_graph_contains_vertex(void *, int, int* OUTPUT);

int jgrapht_graph_add_edge(void *, int, int, int* OUTPUT);

int jgrapht_graph_add_given_edge(void *, int, int, int, int* OUTPUT);

int jgrapht_graph_remove_edge(void *, int, int* OUTPUT);

int jgrapht_graph_contains_edge(void *, int, int* OUTPUT);

int jgrapht_graph_contains_edge_between(void *, int, int, int* OUTPUT);

int jgrapht_graph_degree_of(void *, int, int* OUTPUT);

int jgrapht_graph_indegree_of(void *, int, int* OUTPUT);

int jgrapht_graph_outdegree_of(void *, int, int* OUTPUT);

int jgrapht_graph_edge_source(void *, int, int* OUTPUT);

int jgrapht_graph_edge_target(void *, int, int* OUTPUT);

int jgrapht_graph_is_weighted(void *, int* OUTPUT);

int jgrapht_graph_is_directed(void *, int* OUTPUT);

int jgrapht_graph_is_undirected(void *, int* OUTPUT);

int jgrapht_graph_is_allowing_selfloops(void *, int* OUTPUT);

int jgrapht_graph_is_allowing_multipleedges(void *, int* OUTPUT);

int jgrapht_graph_get_edge_weight(void *, int, double* OUTPUT);

int jgrapht_graph_set_edge_weight(void *, int, double);

int jgrapht_graph_create_all_vit(void *, void** OUTPUT);

int jgrapht_graph_create_all_eit(void *, void** OUTPUT);

int jgrapht_graph_create_between_eit(void *, int, int, void** OUTPUT);

int jgrapht_graph_vertex_create_eit(void *, int, void** OUTPUT);

int jgrapht_graph_vertex_create_out_eit(void *, int, void** OUTPUT);

int jgrapht_graph_vertex_create_in_eit(void *, int, void** OUTPUT);

int jgrapht_graph_as_undirected(void *, void** OUTPUT);

int jgrapht_graph_as_unmodifiable(void *, void** OUTPUT);

int jgrapht_graph_as_unweighted(void *, void** OUTPUT);

int jgrapht_graph_as_edgereversed(void *, void** OUTPUT);

// graph metrics

int jgrapht_graph_metrics_diameter(void *, double* OUTPUT);

int jgrapht_graph_metrics_radius(void *, double* OUTPUT);

int jgrapht_graph_metrics_girth(void *, int* OUTPUT);

int jgrapht_graph_metrics_triangles(void *, long long int* OUTPUT);

int jgrapht_graph_metrics_measure_graph(void *, double* OUTPUT, double* OUTPUT, void** OUTPUT, void** OUTPUT, void** OUTPUT, void** OUTPUT);

// graph path 

int jgrapht_graphpath_get_fields(void *, double* OUTPUT, int* OUTPUT, int* OUTPUT, void** OUTPUT);

// graph test

int jgrapht_graph_test_is_empty(void *, int* OUTPUT);

int jgrapht_graph_test_is_simple(void *, int* OUTPUT);

int jgrapht_graph_test_has_selfloops(void *, int* OUTPUT);

int jgrapht_graph_test_has_multipleedges(void *, int* OUTPUT);

int jgrapht_graph_test_is_complete(void *, int* OUTPUT);

int jgrapht_graph_test_is_weakly_connected(void *, int* OUTPUT);

int jgrapht_graph_test_is_strongly_connected(void *, int* OUTPUT);

int jgrapht_graph_test_is_tree(void *, int* OUTPUT);

int jgrapht_graph_test_is_forest(void *, int* OUTPUT);

int jgrapht_graph_test_is_overfull(void *, int* OUTPUT);

int jgrapht_graph_test_is_split(void *, int* OUTPUT);

int jgrapht_graph_test_is_bipartite(void *, int* OUTPUT);

int jgrapht_graph_test_is_cubic(void *, int* OUTPUT);

int jgrapht_graph_test_is_eulerian(void *, int* OUTPUT);

int jgrapht_graph_test_is_chordal(void *, int* OUTPUT);

int jgrapht_graph_test_is_weakly_chordal(void *, int* OUTPUT);

int jgrapht_graph_test_has_ore(void *, int* OUTPUT);

int jgrapht_graph_test_is_trianglefree(void *, int* OUTPUT);

int jgrapht_graph_test_is_perfect(void *, int* OUTPUT);

int jgrapht_graph_test_is_planar(void *, int* OUTPUT);

int jgrapht_graph_test_is_kuratowski_subdivision(void *, int* OUTPUT);

int jgrapht_graph_test_is_k33_subdivision(void *, int* OUTPUT);

int jgrapht_graph_test_is_k5_subdivision(void *, int* OUTPUT);

// handles

int jgrapht_handles_destroy(void *);

int jgrapht_handles_get_ccharpointer(void *, char** OUTPUT);

// importers

int jgrapht_import_file_dimacs(void *, char*, int);

int jgrapht_import_string_dimacs(void *, char*, int);

int jgrapht_import_file_gml(void *, char*, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_gml(void *, char*, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_json(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_json(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_csv(void *, char*, void *LONG_TO_FUNCTION_POINTER, csv_format_t, int, int, int);

int jgrapht_import_string_csv(void *, char*, void *LONG_TO_FUNCTION_POINTER, csv_format_t, int, int, int);

int jgrapht_import_file_gexf(void *, char*, void *LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_gexf(void *, char*, void *LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_graphml_simple(void *, char*, void * LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_graphml_simple(void *, char*, void *LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_graphml(void *, char*, void *LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_graphml(void *, char*, void *LONG_TO_FUNCTION_POINTER, int, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_dot(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_dot(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_file_graph6sparse6(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

int jgrapht_import_string_graph6sparse6(void *, char*, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER, void *LONG_TO_FUNCTION_POINTER);

// isomorphism

int jgrapht_isomorphism_exec_vf2(void *, void *, int* OUTPUT, void** OUTPUT);

int jgrapht_isomorphism_exec_vf2_subgraph(void *, void *, int* OUTPUT, void** OUTPUT);

int jgrapht_isomorphism_graph_mapping_edge_correspondence(void *, int, int, int* OUTPUT, int* OUTPUT);

int jgrapht_isomorphism_graph_mapping_vertex_correspondence(void *, int, int, int* OUTPUT, int* OUTPUT);

// iterators

int jgrapht_it_next_int(void *, int* OUTPUT);

int jgrapht_it_next_double(void *, double* OUTPUT);

int jgrapht_it_next_object(void *, void** OUTPUT);

int jgrapht_it_hasnext(void *, int* OUTPUT);

// list

int jgrapht_list_create(void** OUTPUT);

int jgrapht_list_it_create(void *, void** OUTPUT);

int jgrapht_list_size(void *, int* OUTPUT);

int jgrapht_list_int_add(void *, int, int* OUTPUT);

int jgrapht_list_double_add(void *, double, int* OUTPUT);

int jgrapht_list_edge_pair_add(void *, int, int, int* OUTPUT);

int jgrapht_list_edge_triple_add(void *, int, int, double, int* OUTPUT);

int jgrapht_list_int_remove(void *, int);

int jgrapht_list_double_remove(void *, double);

int jgrapht_list_int_contains(void *, int, int* OUTPUT);

int jgrapht_list_double_contains(void *, double, int* OUTPUT);

int jgrapht_list_clear(void *);

// map

int jgrapht_map_create(void** OUTPUT);

int jgrapht_map_linked_create(void** OUTPUT);

int jgrapht_map_keys_it_create(void *, void** OUTPUT);

int jgrapht_map_size(void *, int* OUTPUT);

int jgrapht_map_values_it_create(void *, void** OUTPUT);

int jgrapht_map_int_double_put(void *, int, double);

int jgrapht_map_int_int_put(void *, int, int);

int jgrapht_map_int_double_get(void *, int, double* OUTPUT);

int jgrapht_map_int_int_get(void *, int, int* OUTPUT);

int jgrapht_map_int_contains_key(void *, int, int* OUTPUT);

int jgrapht_map_int_double_remove(void *, int, double* OUTPUT);

int jgrapht_map_int_int_remove(void *, int, int* OUTPUT);

int jgrapht_map_clear(void *);

// matching

int jgrapht_matching_exec_greedy_general_max_card(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_custom_greedy_general_max_card(void *, int, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_edmonds_general_max_card_dense(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_edmonds_general_max_card_sparse(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_greedy_general_max_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_custom_greedy_general_max_weight(void *, int, double, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_pathgrowing_max_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_blossom5_general_max_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_blossom5_general_min_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_blossom5_general_perfect_max_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_blossom5_general_perfect_min_weight(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_bipartite_max_card(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_bipartite_perfect_min_weight(void *, void *, void *, double* OUTPUT, void** OUTPUT);

int jgrapht_matching_exec_bipartite_max_weight(void *, double* OUTPUT, void** OUTPUT);

// mst

int jgrapht_mst_exec_kruskal(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_mst_exec_prim(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_mst_exec_boruvka(void *, double* OUTPUT, void** OUTPUT);

// partition

int jgrapht_partition_exec_bipartite(void *, int* OUTPUT, void** OUTPUT, void** OUTPUT);

// planarity

int jgrapht_planarity_exec_boyer_myrvold(void *, int* OUTPUT, void** OUTPUT, void** OUTPUT);

int jgrapht_planarity_embedding_edges_around_vertex(void *, int, void** OUTPUT);

// scoring

int jgrapht_scoring_exec_alpha_centrality(void *, void** OUTPUT);

int jgrapht_scoring_exec_custom_alpha_centrality(void *, double, double, int, double, void** OUTPUT);

int jgrapht_scoring_exec_betweenness_centrality(void *, void** OUTPUT);

int jgrapht_scoring_exec_custom_betweenness_centrality(void *, int, void** OUTPUT);

int jgrapht_scoring_exec_closeness_centrality(void *, void** OUTPUT);

int jgrapht_scoring_exec_custom_closeness_centrality(void *, int, int, void** OUTPUT);

int jgrapht_scoring_exec_harmonic_centrality(void *, void** OUTPUT);

int jgrapht_scoring_exec_custom_harmonic_centrality(void *, int, int, void** OUTPUT);

int jgrapht_scoring_exec_pagerank(void *, void** OUTPUT);

int jgrapht_scoring_exec_custom_pagerank(void *, double, int, double, void** OUTPUT);

// set

int jgrapht_set_create(void** OUTPUT);

int jgrapht_set_linked_create(void** OUTPUT);

int jgrapht_set_it_create(void *, void** OUTPUT);

int jgrapht_set_size(void *, int* OUTPUT);

int jgrapht_set_int_add(void *, int, int* OUTPUT);

int jgrapht_set_double_add(void *, double, int* OUTPUT);

int jgrapht_set_int_remove(void *, int);

int jgrapht_set_double_remove(void *, double);

int jgrapht_set_int_contains(void *, int, int* OUTPUT);

int jgrapht_set_double_contains(void *, double, int* OUTPUT);

int jgrapht_set_clear(void *);

// shortest paths

int jgrapht_sp_exec_dijkstra_get_path_between_vertices(void *, int, int, void** OUTPUT);

int jgrapht_sp_exec_bidirectional_dijkstra_get_path_between_vertices(void *, int, int, void** OUTPUT);

int jgrapht_sp_exec_dijkstra_get_singlesource_from_vertex(void *, int, void** OUTPUT);

int jgrapht_sp_exec_bellmanford_get_singlesource_from_vertex(void *, int, void** OUTPUT);

int jgrapht_sp_exec_bfs_get_singlesource_from_vertex(void *, int, void** OUTPUT);

int jgrapht_sp_exec_johnson_get_allpairs(void *, void** OUTPUT);

int jgrapht_sp_exec_floydwarshall_get_allpairs(void *, void** OUTPUT);

int jgrapht_sp_singlesource_get_path_to_vertex(void *, int, void** OUTPUT);

int jgrapht_sp_allpairs_get_path_between_vertices(void *, int, int, void** OUTPUT);

int jgrapht_sp_allpairs_get_singlesource_from_vertex(void *, int, void** OUTPUT);

int jgrapht_sp_exec_astar_get_path_between_vertices(void *, int, int, void *LONG_TO_FUNCTION_POINTER, void** OUTPUT);

int jgrapht_sp_exec_bidirectional_astar_get_path_between_vertices(void *, int, int, void *LONG_TO_FUNCTION_POINTER, void** OUTPUT);

int jgrapht_sp_exec_astar_alt_heuristic_get_path_between_vertices(void *, int, int, void *, void** OUTPUT);

int jgrapht_sp_exec_bidirectional_astar_alt_heuristic_get_path_between_vertices(void *, int, int, void *, void** OUTPUT);

int jgrapht_sp_exec_yen_get_k_loopless_paths_between_vertices(void *, int, int, int, void** OUTPUT);

int jgrapht_sp_exec_eppstein_get_k_paths_between_vertices(void *, int, int, int, void** OUTPUT);

// spanner

int jgrapht_spanner_exec_greedy_multiplicative(void *, int, double* OUTPUT, void** OUTPUT);

// tour 

int jgrapht_tour_tsp_random(void *, long long int, void** OUTPUT);

int jgrapht_tour_tsp_greedy_heuristic(void *, void** OUTPUT);

int jgrapht_tour_tsp_nearest_insertion_heuristic(void *, void** OUTPUT);

int jgrapht_tour_tsp_nearest_neighbor_heuristic(void *, long long int, void** OUTPUT);

int jgrapht_tour_metric_tsp_christofides(void *, void** OUTPUT);

int jgrapht_tour_metric_tsp_two_approx(void *, void** OUTPUT);

int jgrapht_tour_tsp_held_karp(void *, void** OUTPUT);

int jgrapht_tour_hamiltonian_palmer(void *, void** OUTPUT);

int jgrapht_tour_tsp_two_opt_heuristic(void *, int, double, long long int, void** OUTPUT);

int jgrapht_tour_tsp_two_opt_heuristic_improve(void *, double, long long int, void** OUTPUT);

// traverse

int jgrapht_traverse_create_bfs_from_all_vertices_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_bfs_from_vertex_vit(void *, int, void** OUTPUT);

int jgrapht_traverse_create_lex_bfs_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_dfs_from_all_vertices_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_dfs_from_vertex_vit(void *, int, void** OUTPUT);

int jgrapht_traverse_create_topological_order_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_random_walk_from_vertex_vit(void *, int, void** OUTPUT);

int jgrapht_traverse_create_custom_random_walk_from_vertex_vit(void *, int, int, long long int, long long int, void** OUTPUT);

int jgrapht_traverse_create_max_cardinality_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_degeneracy_ordering_vit(void *, void** OUTPUT);

int jgrapht_traverse_create_closest_first_from_vertex_vit(void *, int, void** OUTPUT);

int jgrapht_traverse_create_custom_closest_first_from_vertex_vit(void *, int, double, void** OUTPUT);

// vertex cover

int jgrapht_vertexcover_exec_greedy(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_greedy_weighted(void *, void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_clarkson(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_clarkson_weighted(void *, void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_edgebased(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_baryehudaeven(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_baryehudaeven_weighted(void *, void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_exact(void *, double* OUTPUT, void** OUTPUT);

int jgrapht_vertexcover_exec_exact_weighted(void *, void *, double* OUTPUT, void** OUTPUT);

