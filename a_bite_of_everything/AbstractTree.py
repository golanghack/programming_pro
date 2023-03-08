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
        
    def _list_with_levels(self, level: int, trees: list):
        trees.append('-*-' * level + str(self.data))
        for child in self.children:
            child._list_with_levels(level + 1, trees)
            
    def __str__(self) -> str:
        trees = []
        self._list_with_levels(0, trees)
        return '\n'.join(trees)
    
    def __eq__(self, other) -> bool:
        return self.data == other.data and self.children == other.children
    

tree = Tree(['a', ['b', ['c', ['d']]], ['e', ['f'], ['g', ['h']]]])
print(tree)    
    
    