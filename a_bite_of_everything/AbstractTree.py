#! /usr/bin/env python3 

class Tree:
    """Abstract Tree.
    :param -> height -> heght tree
    :param -> preorder traversal
    :param -> postorder traversal
    :param -> layer_order -> layer order traversal.
    """
    
    def __init__(self, list_for_tree: list) -> None:
        iterator = iter(list_for_tree)
        self.data = next(iterator)
        self.children = [Tree(child) for child in iterator]
        
    
    