#! /usr/bin/env python3 

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

if __name__ == '__main__':
    lst = [1, 2, 3, 3, 4, 6, 8, 12]
    new_lst = insert_list(lst, 0)
    print(new_lst)