

from functools import reduce 
import operator
from typing import Callable, List

options = {
    '+': operator.add, 
    '-': operator.add, 
    '*': operator.mul, 
    '/': operator.truediv,
}

def math_mutator(tree: List) -> Callable:
    """Mutation mathematical sentence to json tree"""

    if not isinstance(tree, list):
        return tree
    option = options[tree.pop(0)]
    return reduce(option, map(math_mutator, tree))