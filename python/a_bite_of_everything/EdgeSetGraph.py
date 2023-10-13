#! /usr/bin/env python3 

class EdgeSetGraph:
    """
    method -> vertices -> return iterator for vertices
    method -> edges -> return iterator set edges 
    method -> add_vertex(vertex) -> add new vertex in graph
    method -> add_edge(u, v), u, v -keys vertex add new edge
    method -> remove_edge(u, v) -> remove edge u-v from graph
    method -> __contains__(vertex) -> boolean. True if vertex in graph
    method -> has_edge(u, v) -> boolean. True if edge(u, v) in graph
    method -> nbrs(v) -> iterator set neighbours
    method -> __len__() -> return vertex in graph.
    """

    def __init__(self, vertex = (), edge = ()):
        self._vertex = set()
        self._edge = set()

        for v in vertex: 
            self.add_vertex(vertex)
        for u, v in edge:
            self.add_edge(u, v)

    def vertices(self):
        return iter(self._vertex)

    def edges(self):
        return iter(self._edge)
    
    def add_vertex(self, vrtx):
        self._vertex.add(vrtx)

    def add_edge(self, u, v):
        self._edge.add((u, v))

    def remove_edge(self, u, v):
        self._edge.remove((u, v))

    def __contains__(self, v):
        return v in self._vertex

    def has_edge(self, u, v):
        return (u, v) in self._edge

    def nbrs(self, v):
        return (w for u, w in self._edge if u == v)

    def __len__(self):
        return len(self._vertex)
