#! /usr/bin/env python3 

""" 
TASK 

Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.
"""

def get_number(message: str) -> str:
    line = input(message)
    number = []
    for i in line:
        if i in ['0', '1']:
            number.append(i)
        else:
            raise ValueError('\nUncorrect number! Try Again.')
    return number
        
def from_list_to_string(lst: list) -> str:
    return ''.join(map(str, lst))

def from_binary_to_decimal(number):
    decimal = 0
    for i in number:
        decimal = decimal + int(number[int(i)]) * (2 ** (len(number) - int(i) - 1))
    return decimal
    
if __name__ == '__main__':
    list_number = get_number('Enter number -> ')
    string_number = from_list_to_string(list_number)
    convert = from_binary_to_decimal(string_number)
    print(f'You entered number on 2 base -> {list_number}')
    print(f'number to 10 base -> {convert}')