#! /usr/bin/env python3 

import copy


class Graph:
    
    def __init__(self, name: str, connections: list) -> None:
        self.name = name
        self.connections = connections
        
    def add_connection(self, other: str) -> None:
        self.connections.append(other)
        
    def __repr__(self) -> str:
        return f'Graph(name={self.name}, id={id(self)})'
    
    def __deepcopy__(self, memo):
        print(f'\nCalling __deepcopy__ for {self!r}')
        if self in memo:
            existing = memo.get(self)
            print(f'---Already copied to {existing!r}')
            return existing
        print('---Memo dict---')
        if memo:
            for k, v in memo.items():
                print(f'----{k}:{v}')
        else:
            print('---- (empty)')
            
        dublicate = Graph(copy.deepcopy(self.name, memo), [])
        print(f'--- Copying to new object {dublicate}')
        memo[self] = dublicate
        
        for c in self.connections:
            dublicate.add_connection(copy.deepcopy(c, memo))
        return dublicate
    
root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])

root.add_connection(a)
root.add_connection(b)

dublicate = copy.deepcopy(root)