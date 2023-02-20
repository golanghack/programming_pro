#! /usr/bin/env python3 

def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    set_for_my_list = set()
    for element in any_list:
        if element in set_for_my_list:
            return True
        set_for_my_list.add(element)
        return False
    
