#! /usr/bin/env python3

def insert_binary_tree(x: int, T: list) -> list:
    """Inserting element in tree."""
    
    if T == []:
        T.extend([x[0], x[1], [], []])
    else:
        if x[0] < T[0]:
            if T[2] == []:
                T[2] = [x[0], x[1], [], []]
            else:
                insert_binary_tree(x, T[2])
        else:
            if T[3] == []:
                T[3] = [x[0], x[1], [], []]
            else:
                insert_binary_tree(x, T[3])