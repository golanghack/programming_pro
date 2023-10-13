#! /usr/bin/env python3 

def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    n_range = len(any_list)
    return any(any_list[i] == any_list[j] for i in range(1, n_range) for j in range(i))

