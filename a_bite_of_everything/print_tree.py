#! /usr/bin/env python3 

tree = ['c', ['a', ['b', 'c', 'd']], ['o', ['p']]]

def print_tree_without_iterator(tree):
    zero = tree[0]
    print(zero)
    for child in range(1, len(tree)):
        print_tree_without_iterator(tree[child])
        

def print_tree_with_iterator(tree):
    iterator = iter(tree)
    print(next(iterator))
    for child in iterator:
        print_tree_with_iterator(child)
        
print(f'Print tree without iterator -> {print_tree_without_iterator(tree)}')
print(f'Print tree with iterator -> {print_tree_with_iterator(tree)}')
    