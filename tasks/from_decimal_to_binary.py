#! /usr/bin/env python3 

""" 
TASK 

Write a program that converts a decimal (base 10) number to binary (base 2). Read the
decimal number from the user as an integer and then use the division algorithm shown
below to perform the conversion. When the algorithm completes, result contains the
binary representation of the number. Display the result, along with an appropriate
message.3.4 Exercises
55
Let result be an empty string
Let q represent the number to convert
repeat
Set r equal to the remainder when q is divided by 2
Convert r to a string and add it to the beginning of result
Divide q by 2, discarding any remainder, and store the result back into q
until q is 0
"""

from util_for_tasks.get_number import get_number

LABEL = '----FROM DECIMAL TO BINARY----'
BASE = get_number('Enter base -> ')

result: str = '' 

input_number = get_number('Enter number -> ')

differention_number = input_number

remainder = differention_number % BASE

result = str(remainder) + result

differention_number = differention_number // BASE

while differention_number > 0:
    remainder = differention_number % BASE
    result = str(remainder) + result
    differention_number = differention_number // BASE
    
print(LABEL)
print(f'You entered number in decimal base -> \n{input_number}')
print(f'Different number to binary base -> \n{result}')

   



