#! /usr/bin/env python3 

def is_palindrome(input_string: str) -> bool:
    """-> return True is string is palindrom"""

    reverse_string = input_string[::-1]
    if reverse_string == input_string:
        return True
    else:
        return False

print(is_palindrome('aba'))
