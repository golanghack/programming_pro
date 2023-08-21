#! /usr/bin/env python3 

"""This parser scan input and testing first char
If first char is char or str different whitespace 
index incrementing
"""

from syntax_parse.skip_space import skip_space

def parse_express(input_s: str, idx: int):
    idx = skip_space(input_s, idx)
    if input_s[idx] == '(':
        # --> LIST
        idx += 1
        l = []
        while True:
            idx = skip_space(input_s, idx)
            if idx >= len(input_s):
                raise Exception('unbalanced!')
            if input_s[idx] == ')':
                idx += 1
                break
            idx, value = parse_express(input_s, idx)
            l.append(value)
        return idx, l 
    elif input_s[idx] == ')':
        raise Exception('bad parenthesis')
    else:
        # --> SYMBOL
        start = idx 
        while idx < len(input_s) and (
            not input_s[idx].isspace()) and input_s[idx] not in '()':
            idx += 1
        if start == idx:
            raise Exception('empty')
        return idx, parse_symbol(input_s[start:idx])