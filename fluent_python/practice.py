"""
example facts:
    m = 3.28 ft
    ft = 12 in
    hr = 60 min
    min = 60 sec

example query:
    2 m = ? in
    13 in = ? m
    13 in = ? hr

(str, float, str) data
(float, str, str) query
float or Exception return

unit_conversion_map: dict = {
    ("m", "ft"): 3.28,
    ("m", "in"): 3.28*12,
    ("ft", "in"): 12,
    ("ft", "m"): 1/3.28,
    ("in", "ft"): 1/12,
    ("in", "m"): 1/(12*3.28),
}

query = (2, "m", "in")

value = query[0]
key = query[1:]
factor = unit_conversion_map[key]

output = value * factor
"""
from queue import Queue
# unit is node, edge is float.

class Node:
    def __init__(self, unit: str):
        self.unit = unit
        self.edges = []
    
    def add_edge(self, multiplier: float, other_unit: str):
        other_node = Node(other_unit)
        edge = Edge(multiplier, other_node)
        self.edges.append(edge)

class Edge:
    def __init__(self, multiplier: float, node: Node):
        self.multiplier = multiplier
        self.node = node
    
def parse_facts(facts: list[tuple[str, float, str]]) -> dict[str, Node]:
    """"""
    facts_storage = {}
    for base_unit, multiplier, quote_unit in facts:
        if base_unit not in facts_storage:
            facts_storage[base_unit] = Node(base_unit)
            facts_storage[base_unit].add_edge(multiplier, quote_unit)
        
        if quote_unit not in facts_storage:
            facts_storage[quote_unit] = Node(quote_unit)
            facts_storage[quote_unit].add_edge(multiplier, base_unit)
    
    return facts_storage
        

def answer_query(query: tuple[float, str, str], facts:list[tuple[str, float, str]]):
    """"""
    unit_converter = parse_facts(facts)

    factor, from_unit, to_unit = query
    
    if from_unit not in unit_converter:
        raise ValueError(f"Unit {from_unit} does not exist in facts.")
    if to_unit not in unit_converter:
        raise ValueError(f"Unit {to_unit} does not exist in facts.")
    if from_unit == to_unit:
        return factor
    
    to_visit = Queue()
    visited = set()
    to_visit.put((to_unit, factor))
    visited.add(from_unit)

    while not to_visit.empty:
        connections = unit_converter[from_unit].edges
        to_unit, factor = to_visit.get()

        for connection in connections:
            other_node = connection.node
            if other_node.unit in visited:
                continue

            multiplier = connection.multiplier
            if other_node.unit == to_unit:
                return factor * multiplier

            visited.add(to_unit)
            factor *= multiplier
            to_visit.put((other_node.unit, factor))
        
        
        
    
    
    


    return None


