#! /usr/bin/env python3 

from AbstractTree import Tree

tree = Tree(['a', ['b', ['c', ['d']]],['e', ['f'], ['g']]])

def print_tree(tree: list):
    print(tree.data)
    for child in tree.children:
        print_tree(child)
        
        
print_tree(tree)
    



