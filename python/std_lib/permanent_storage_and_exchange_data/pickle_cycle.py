#! /usr/bin/env python3 

import pickle

class Node:
    """ 
    Simple double graph.
    """
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections = []
        
    def add_edge(self, node):
        """Create border between set and next nodes."""
        
        self.connections.append(node)
        
    def __iter__(self):
        return iter(self.connections)
    
def preorder_traversal(root, seen=None, parent=None):
    """ 
    Generator. Return borders of graph.
    """
    
    if seen is None:
        seen = set()
    yield (parent, root)
    
    if root in seen:
        return
    seen.add(root)
    
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)
            
def show_edges(root):
    """Printing all border of graph."""
    
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print(f'{parent.name:>5} -> {child.name:>2} ({id(child)})')

# setting nodes        
root = Node('root')

a = Node('a')
b = Node('b')
c = Node('c')

# adding border between graph
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print('ORIGINAL GRAPH -> ')
show_edges(root)

# serialization and deserialization graph for create new nodes 
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\nRELOADED GRAPH -> ')
show_edges(reloaded)