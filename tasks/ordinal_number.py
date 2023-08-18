#! /usr/bin/env python3 

"""TASK 

Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an integer as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the integers between 1 and 12 (inclusive). It should return an
empty string if the function is called with an argument outside of this range. Include
a main program that demonstrates your function by displaying each integer from 1
to 12 and its ordinal number. Your main program should only run when your file has
not been imported into another program.
"""

from util_for_tasks.get_number import get_number

LIST_OF_NUMBERS = ['zero',
                   'first', 
                   'second', 
                   'third', 
                   'fourth', 
                   'fifth', 
                   'sixth', 
                   'seventh', 
                   'eighth', 
                   'ninth',
                   'tenth', 
                   'eleventh', 
                   'twelth', 
                   ]

def print_order_numbers(number: int):
    if number <= 12:
        for i in enumerate(LIST_OF_NUMBERS):
            print('All')
            print(i)
        print()
        print(f'your entered number -> {number}')
        print(f'and ordered number for your number -> {LIST_OF_NUMBERS[number]}')
    return 

if __name__ == '__main__':
    print_order_numbers(get_number('Enter number -> '))
