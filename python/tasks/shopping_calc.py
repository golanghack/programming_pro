#! /usr/bin/env python3 

""" 
TASK 

An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item in an order, and $2.95 for each subsequent item in the same order.
Write a function that takes the number of items in the order as its only parameter.
Return the shipping charge for the order as the function’s result. Include a main
program that reads the number of items purchased from the user and displays the
shipping charge.
"""

from util_for_tasks.get_number import get_number

def main():
    full = full_summ(count_pos)

    print('---FULL SUMM ORDER---')
    print('---------------------')
    print(f'--ORDER---{count_pos}')
    print(f'--------full---${full:.2f}')

FIRST_PRICE = 10.95
SECOND_PRICE = 2.95

count_pos = get_number('Enter count position -> ')

def full_summ(count_pos: int) -> float:
    """Return full summ in order."""
    if count_pos > 1:
        return FIRST_PRICE + ((count_pos - 1) * SECOND_PRICE)
    return FIRST_PRICE

if __name__ == '__main__':
    main()