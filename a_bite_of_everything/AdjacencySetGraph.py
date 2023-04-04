#! /usr/bin/env python3 

class AdjacencySetGraph:

    def __init__(self, v = (), e = ()):
        self._v = set()
        self._nbrs = {}
        for vert in v:
             self.add_vertex(vert)
        for edg in e:
             self.add_edge(*edg)

    def vertices(self):
        return iter(self._v)
    
    def edges(self):
        for u in self._v:
            for v in self.nbrs(u):
                yield (u, v)

    def add_vertex(self, v):
        self._v.add(v)
        self._nbrs[v] = set()

    def add_edge(self, u, v):
        self._nbrs[u].add(v)
    
    def remove_edge(self, u, v):
        self._nbrs[u].remove(v)

    def __contains__(self, v):
        return v in self._nbrs

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def __len__(self):
        return len(self._nbrs)