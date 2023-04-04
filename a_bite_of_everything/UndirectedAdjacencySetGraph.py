#! /usr/bin/env python3 

from AdjacencySetGraph import AdjacencySetGraph

class UndirectedAdjacencySetGraph(AdjacencySetGraph):

    def add_edge(self, u, v):
        AdjacencySetGraph.add_edge(self, u, v)
        AdjacencySetGraph.add_edge(self, v, u)

    def remove_edge(self, u, v):
        AdjacencySetGraph.remove_edge(self, u, v)
        AdjacencySetGraph.remove_edge(self, v, u)
    
    def edges(self):
        E = {frozenset(e) for e in AdjacencySetGraph.edges(self)}
        return iter(E)