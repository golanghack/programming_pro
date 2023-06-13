#! /usr/bin/env python3 

"""  
TASK 

Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in ascending order, with one
value appearing on each line. Use either the sort method or the sorted function
to sort the list.
""" 

from util_for_tasks.get_number import get_number

def parsing_stdin(message: str, list_for_numbers: list) -> int:
    """Return number if number != 0""" 

    switcher = True
    while switcher:
        number = get_number(message)
        if number != 0:
            list_for_numbers.append(number)
        else:
            switcher = False
    return sorted(list_for_numbers)

def main():
    list_numbers = parsing_stdin('Enter number or 0 for exit ', [])
    print(list_numbers)

if __name__ == '__main__':
    main()
        
    