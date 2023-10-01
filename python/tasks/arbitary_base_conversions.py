#! /usr/bin/env python3 

""" 
TASK 

Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user.
""" 

from util_for_tasks.get_number import get_number

COMMON_MESSAGE_FOR_SCREEN = 'You entered numbers from 2 to 16 (may to 32, 64 etc.)'
MESSAGE = 'Enter number '
MESSAGE_FOR_BASE = 'Enter base number -> '
ERROR_MESSAGE = 'You entered non supported integers base! Try Again!'

def universal_convertions(number: int, base: int, upper=False):
    """Universal builder from base to rebase system"""
    
    
    new_number = ''
    full_string_numbers = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(full_string_numbers): 
        return ERROR_MESSAGE
    while number > 0:
        new_number = full_string_numbers[number % base] + new_number
        number //= base
    return new_number.upper() if upper else new_number

def main():
    print(COMMON_MESSAGE_FOR_SCREEN)

    number = get_number(MESSAGE)
    base = get_number(MESSAGE_FOR_BASE)
    result = universal_convertions(number, base)
    print(result)

    
    


if __name__ == '__main__':
    main()

