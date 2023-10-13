#! /usr/bin/env python3 

""" 
TASK 
Write a program that asks the user for an integer four
a three-digit number and the sum of its constituent digits. On the-
example, if the user enters the number 3141, the program should output
next result: 3 + 1 + 4 + 1 = 9.
"""

MESSAGE = 'Enter number -> '

def main() -> None:
    number = user_api(MESSAGE)
    print(f'You entered number -> {number}')
    print(f'Full sum from entered number -> {counting_gigit_of_number(number)}')

def user_api(message_for_user: str) -> int:
    """API for work with user."""
    
    try:
        string_number = input(message_for_user)
        number = int(string_number)
        return number
    except ValueError as err:
        print(f'You entered not valiud number. Error -> {err}. Please, try again.')
    
def counting_gigit_of_number(number: int) -> int:
    """Return summ all digits in number."""
    
    list_digit_from_number = [i for i in str(number)]
    number_list_from_string = [int(j) for j in list_digit_from_number]
    
    result = sum(number_list_from_string)
    return result

if __name__ == '__main__':
    main()