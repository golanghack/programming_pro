#! /usr/bin/env python3 

"""<--MERGING-->"""


def merge(first_lst, second_lst):
    """THis function returns new list sorted with merged"""
    """ 
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> merge(a, b)
    [1, 2, 3, 4, 5, 6]
    """
    
    new_list = []
    while (min(len(first_lst), len(second_lst)) > 0):
        if first_lst[0] > second_lst[0]:
            to_insert = second_lst.pop(0)
            new_list.append(to_insert)
        if first_lst[0] <= second_lst[0]:
            to_insert = first_lst.pop(0)
            new_list.append(to_insert)
    if (len(first_lst) > 0):
        for i in first_lst:
            new_list.append(i)
    if (len(second_lst) > 0):
        for i in second_lst:
            new_list.append(i)
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()