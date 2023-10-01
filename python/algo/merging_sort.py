#! /usr/bin/env python3 

"""<--MERGING SORT ALGO-->"""

import math 

def merge(first_lst, second_lst):
    """THis function returns new list sorted with merged
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

def mergesort_two_elements_in_lists(lst):
    """Return sorted lst include two elements
    
    >>> a = [4, 2]
    >>> mergesort_two_elements_in_lists(a)
    [2, 4]
    
    """
    
    new_lst = []
    if (len(lst) == 1):
        new_lst = lst
    else:
        first = lst[:math.floor(len(lst) / 2)]
        second = lst[math.floor(len(lst) / 2):]
        new_lst = merge(first, second)
    return new_lst

def mergesort_four_elements(lst):
    """Return sorted list with merging
    
    >>> a = [2, 3, 4, 1]
    >>> mergesort_four_elements(a)
    [1, 2, 3, 4]
    """
    
    new_lst = []
    if(len(lst) == 1):
        new_lst = lst 
    else:
        first = mergesort_two_elements_in_lists(lst[:math.floor(len(lst) / 2)])
        second = mergesort_two_elements_in_lists(lst[math.floor(len(lst) / 2):])
        new_lst = merge(first, second)
    return new_lst

def merge_sort(lst):
    """SOrting with merging
    >>> a = [4, 1, 3, 5, 6, 7, 9]
    >>> merge_sort(a)
    [1, 3, 4, 5, 6, 7, 9]
    """
    
    new_lst = []
    if (len(lst) == 1):
        new_lst = lst
    else:
        first = merge_sort(lst[:math.floor(len(lst) / 2)])
        second = merge_sort(lst[math.floor(len(lst) / 2):])
        new_lst = merge(first, second)
    return new_lst

if __name__ == '__main__':
    import doctest
    doctest.testmod()