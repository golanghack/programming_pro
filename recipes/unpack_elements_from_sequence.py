#! /usr/bin/env python3 

""" 
You need to unpack N elements from an iterable, but that object can
may contain more than N elements, which causes the exception 'too many values to
unpack'.

"""

def unpack_first_last(list_with_elements: list) -> list:
    """Unpackage elements from sequence."""
    
    first, *second, end = list_with_elements
    return first, second, end

