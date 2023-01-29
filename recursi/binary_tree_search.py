#! /usr/bin/env python3 

"""Binary Tree search algorithm."""

def binary_tree_search(T: list, key: int) -> int:
    """Searching in tree."""
    
    if T == []:
        return None
    elif T[0] == key:
        return T[1] # return the root item
    elif key < T[0]:
        return binary_tree_search(T[2], key) # search in left subtree
    else:
        return binary_tree_search(T[3], key) # search in right subtree
    
