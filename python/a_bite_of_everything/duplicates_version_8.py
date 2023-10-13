#! /usr/bin/env python3 

def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    set_for_my_list = set()
    return any(element in set_for_my_list 
               or set_for_my_list.add(element) 
               for element in any_list)
    
    