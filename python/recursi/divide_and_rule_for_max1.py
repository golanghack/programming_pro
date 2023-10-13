#! /usr/bin/env python3 

def max_list_lenght_divide_and_rule(a: list) -> int:
    """Find maximum in list."""
    
    upper = a[-1]
    lower = a[0]
    
    if len(a) == 1:
        return a[0]
    else:
        middle = (upper + lower) // 2
        middle_right = max_list_lenght_divide_and_rule(a[0:middle])
        middle_left = max_list_lenght_divide_and_rule(a[middle:len(a)])
        return max(middle_right, middle_left)
    
list_ = [1, 3, 5, 6]
print(max_list_lenght_divide_and_rule(list_))
        