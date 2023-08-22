#! /usr/bin/env python3 

"""Expression Evaulation
 -> look at the first item on the list and decide what the operation is;
 -> evaulate the rest of the items recursively;
 -> perform the operation;
""" 

import operator
from typing import List

def prefetch_eval(node: List) -> List:
    if len(node) == 0:
        err_message = 'empty target list'
        raise ValueError(err_message)
    # bool, number, string...
    if len(node) == 2 and node[0] == 'val':
        return node[1]
    # binary operators
    binary_operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        'eq': operator.eq,
        'ne': operator.ne,
        'ge': operator.ge,
        'gt': operator.gt,
        'le': operator.le,
        'lt': operator.lt,
        'and': operator.and_,
        'or': operator.or_,
    }

    unary_operators = {
        '-': operator.neg,
        'not': operator.not_,
    }

    if len(node) == 3 and node[0] in binary_operators:
        single_operator = binary_operators[node[0]]
        return single_operator(prefetch_eval(node[1]), prefetch_eval(node[2]))

    if len(node) == 2 and node[0] in unary_operators:
        single_operator = unary_operators[node[0]]
        return single_operator(prefetch_eval(node[1]))

    # conditionals
    if len(node) == 4 and node[0] == '?':
        _, cond, yes, no = node
        if prefetch_eval(cond):
            return prefetch_eval(yes)
        else:
            return prefetch_eval(no)
    
    # output
    if node[0] == 'print':
        return print(*(prefetch_eval(val) for val in node[1:]))
    raise ValueError('did not find pattern expression')