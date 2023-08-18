#! /usr/bin/env python3 

""" 
TASK 

The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m. There are several algorithms that can be
used to solve this problem, including:
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m
Write a program that reads two positive integers from the user and uses this algorithm
to determine and report their greatest common divisor.
"""

message_for_user = 'Enter number -> '

def get_number(message):
    try:
        line = input(message)
        number = int(line)
        return number
    except ValueError as err:
        print(f'You entered uncorrect number(-s)-> {err}. Try Again.')

def gdc(number_one, number_two):
    if number_one < number_two:
        b = number_one
    else:
        b = number_two
    
    while (number_one % 2 != 0) or (number_two % 2 != 0):
        b = b - 1
    return b 

def main():
    number_one = get_number(message_for_user)
    number_two = get_number(message_for_user)
    
    result = gdc(number_one, number_two)
    print(f'You entered numbers {number_one} and {number_two}')
    print()
    print(f'Greatest common divider -> {result}') 
    
if __name__ == '__main__':
    main()