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
    
    def height(self) -> int:
        if len(self.children) == 0:
            return 0 
        else:
            return 1 + max(child.height() for child in self.children)
        
    def __contains__(self, k):
        return self.data == k or any(k in child for child in self.children)
    
    def print_post_order(self, tree:list):
        for ch in self.children:
            ch.print_post_order(ch)
            print(tree.data)

    def preorder(self):
        yield self.data
        for child in self.children:
            for data in child.preorder():
                yield data
    
    __iter__ = preorder
    
    # close 
    def _preorder(self):
        yield self
        for child in self.children:
            for descedent in child._preorder():
                yield descedent
                
tree = Tree(['a', ['b', ['c', ['d']]], ['e', ['f'], ['g', ['h']]]])
print(tree)    
    
    