#! /usr/bin/env python3 

from pprint import pprint

class Node:
    
    def __init__(self, name: str, contents: list=[]) -> None:
        self.name = name
        self.contents = contents
        
    def __repr__(self) -> str:
        return ('Node(' + repr(self.name) + ', ' + repr(self.contents) + ')')
    
trees: list = [
    Node('node-1'),
    Node('node-2', [Node('node-2-1')]),
    Node('node-3', [Node('node-3-1')]),
]

pprint(trees)