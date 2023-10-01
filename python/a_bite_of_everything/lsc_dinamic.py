#! /usr/bin/env python3 

def lcs(X: str, Y: str) -> str:
    t = {}
    
    for i in range(len(X) + 1):
        t[(i, 0)] = ''
    for j in range(len(Y) + 1):
        t[(0, j)] = ''
        
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                t[(i + 1, j + 1)] = t[(i, j)] + x 
            else:
                t[(i + 1, j + 1)] = max([t[(i, j + 1)], t[(i + 1, j)]], key=len)
    return t[(len(X), len(Y))]
