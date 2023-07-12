#! /usr/bin/env python3 

def fixed(some_object) -> bool:
    """Return True if object hash and False""" 

    try:
        hash(some_object)
    except TypeError:
        return False
    return True

