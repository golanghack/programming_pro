#! /usr/bin/env python3 

def max_list_limits_with_divide_and_rule(a: list, lower: int, upper: int) -> int:
    """Find maximum in list."""
    
    if lower == upper:
        return a[lower]
    else:
        middle = (upper + lower) // 2
        max_1 = max_list_limits_with_divide_and_rule(a, lower, upper)
        max_2 = max_list_limits_with_divide_and_rule(a, middle + 1, upper)
        return max(max_1, max_2)
    
list_ = [3, 5, 6, 9]
print(max_list_limits_with_divide_and_rule(list_, 5, 4))
    