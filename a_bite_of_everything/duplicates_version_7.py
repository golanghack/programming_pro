#! /usr/bin/env python3 

def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    return len(any_list) != len(set(any_list))
