#! /usr/bin/env python3 

from EdgeSetGraph import EdgeSetGraph

class UndirectedEdgeSetGraph(EdgeSetGraph):

    def add_edge(self, u, v):
        self._edge.add(frozenset({u, v}))

    def remove_edge(self, u, v):
        self._edge.remove(frozenset({u, v}))

    def nbrs(self, v):
        for u, w in self._edge:
            if u == v:
                yield w 
            elif w == v:
                yield u 