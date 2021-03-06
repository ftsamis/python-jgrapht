import pytest

from jgrapht import create_graph
from jgrapht.io.importers import read_gexf, parse_gexf
from jgrapht.io.exporters import write_gexf, generate_gexf

input1=r"""<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://www.gexf.net/1.2draft"
    version="1.2" 
    xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <graph defaultedgetype="undirected">
        <nodes>
            <node id="1" label="1"/>
            <node id="2" label="2"/>
            <node id="3" label="3"/>
        </nodes>
        <edges>
            <edge id="1" source="2" target="3" />
            <edge id="0" source="1" target="2" />
            <edge id="2" source="3" target="1" />
        </edges>
        </graph>
</gexf>
"""

expected=r"""<?xml version="1.0" encoding="UTF-8"?><gexf xmlns="http://www.gexf.net/1.2draft" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <graph defaultedgetype="directed">
        <nodes>
            <node id="0" label="0"/>
            <node id="1" label="1"/>
            <node id="2" label="2"/>
            <node id="3" label="3"/>
        </nodes>
        <edges>
            <edge id="0" source="0" target="1"/>
            <edge id="1" source="0" target="2"/>
            <edge id="2" source="0" target="3"/>
            <edge id="3" source="2" target="3"/>
        </edges>
    </graph>
</gexf>
"""

def test_input_gexf(tmpdir):
    g = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)
    parse_gexf(g, input1, validate_schema=True)
    
    assert len(g.vertices()) == 3
    assert len(g.edges()) == 3


def test_input_gexf_with_renumbering(tmpdir):
    g = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    def import_id(x): 
        return int(x)+5

    parse_gexf(g, input1, import_id_cb=import_id, validate_schema=True)
    
    assert len(g.vertices()) == 3
    assert len(g.edges()) == 3

    assert not g.contains_vertex(1)
    assert g.contains_vertex(6)


def test_export_import(tmpdir):

    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=True, weighted=True)

    for i in range(0, 10):
        g.add_vertex(i)

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
    g.create_edge(9, 1, weight=33.3)

    assert len(g.edges()) == 18

    tmpfile = tmpdir.join('gexf.out')
    tmpfilename = str(tmpfile)

    attrs = [('cost', 'edge', 'double', None), ('name', 'node', 'string', None)]

    v_dict = { 
        0: { 'name': 'κόμβος 0' }, 
	    1: { 'name': 'node 1'   } 
    }
    e_dict = {
        17: {
            'cost': '48.5'
        }
    }

    write_gexf(g, tmpfilename, attrs=attrs, per_vertex_attrs_dict=v_dict, per_edge_attrs_dict=e_dict, export_edge_weights=True)

    # read back 

    g1 = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=True, weighted=True)

    def va_cb(vertex, attribute_name, attribute_value):
        print('Vertex {}, attr {}, value {}'.format(vertex, attribute_name, attribute_value))
        if vertex == 0:
            if attribute_name == 'name': 
                assert attribute_value == 'κόμβος 0'
        if vertex == 1:
            if attribute_name == 'name': 
                assert attribute_value == 'node 1'

    def ea_cb(edge, attribute_name, attribute_value):
        print('Edge {}, attr {}, value {}'.format(edge, attribute_name, attribute_value))
        if edge == 17: 
            if attribute_name == 'cost': 
                assert attribute_value == '48.5'
            if attribute_name == 'weight': 
                assert attribute_value == '33.3'
            if attribute_name == 'source': 
                assert attribute_value == '9'
            if attribute_name == 'target': 
                assert attribute_value == '1'
            if attribute_name == 'id': 
                assert attribute_value == '17'                

    read_gexf(g1, tmpfilename, vertex_attribute_cb=va_cb, edge_attribute_cb=ea_cb)

    assert g1.vertices() == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert g1.contains_edge_between(6, 7)
    assert not g1.contains_edge_between(6, 8)
    assert len(g1.edges()) == 18

    assert g1.get_edge_weight(17) == 33.3

def test_output_to_string(): 
    g = create_graph(directed=True, allowing_self_loops=False, allowing_multiple_edges=True, weighted=False)

    g.add_vertices_from(range(0,4))

    g.create_edge(0, 1)
    g.create_edge(0, 2)
    g.create_edge(0, 3)
    g.create_edge(2, 3)

    out = generate_gexf(g)

    assert out.splitlines() == expected.splitlines()
