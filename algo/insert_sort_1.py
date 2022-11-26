#! /usr/bin/env python3 

"""<--INSERT SORT 1-->"""

old_lst = [8, 4, 6, 1, 2, 5, 3, 7]

def insert_list(lst, to_insert):
    """insert_list sorting with insert"""
    
    check_location_number = len(lst) - 1
    insert_number = 0
    
    #main algo while 
    while(check_location_number >= 0):
        if to_insert > lst[check_location_number]:
            insert_number = check_location_number + 1
            check_location_number = -1
        if to_insert == 0:
            lst[0] = to_insert
            del(lst[0])
            break
        check_location_number -= 1
    lst.insert(insert_number, to_insert)
    return lst 

def insertion_list(old_lst):
    """insert_list sorting with insert"""
    new_lst = []
   
    while len(old_lst) > 0:
        to_insert = old_lst.pop(0)
        new_lst = insert_list(new_lst, to_insert)
    return new_lst
       

if __name__ == '__main__':
    sorted_lst = insertion_list(old_lst)
    print(sorted_lst)