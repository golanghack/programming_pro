#! /usr/bin/env python3 

"""TASK 

Write a function that takes a string, s, as its first parameter, and the width of the
window in characters, w, as its second parameter. Your function will return a new
string that includes whatever leading spaces are needed so that s will be centered in
the window when the new string is printed. The new string should be constructed in
the following manner:
• If the length of s is greater than or equal to the width of the window then s should
be returned.4.5 Exercises
69
• If the length of s is less than the width of the window then a string containing
(len(s) - w) // 2 spaces followed by s should be returned.
Write a main program that demonstrates your function by displaying multiple
strings centered in the window.
"""

import textwrap
from util_for_tasks.get_number import get_number

def get_string(message: str) -> str:
    user_string = input(message)
    return user_string

def get_width(message: str) -> int:
    width = get_number(message)
    return width

def print_examples():
    print('Examples')
    print('string -> aaa, width - 13')
    print('          aaa          ')
    print()
    print('string -> aaa, width - 1')
    print('aaa')
    print()
    print('string -> aaa, width -> 7')
    print('  aaa  ')

def drow():
    user_string = get_string('Enter string -> ')
    width = get_width('Enter width window -> ')
    part_width = (len(user_string) - width) * (-1) // 2
    content = ' ' * part_width

    if len(user_string) >= width:
        return user_string
    else:    
        return content + user_string

def main():
    print_examples()
    print(drow())

if __name__ == '__main__':
    main()
