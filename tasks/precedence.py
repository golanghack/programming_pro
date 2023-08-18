#! /usr/bin/env python3 

"""
TASK 

Write a function named precedence that returns an integer representing the prece-
dence of a mathematical operator. A string containing the operator will be passed to
the function as its only parameter. Your function should return 1 for + and -, 2 for *
and /, and 3 for ˆ. If the string passed to the function is not one of these operators
then the function should return -1. Include a main program that reads an operator
from the user and either displays the operator’s precedence or an error message indi-
cating that the input was not an operator. Your main program should only run when
the file containing your solution has not been imported into another program.
In this exercise, along with others that appear later in the book, we will use
ˆ to represent exponentiation. Using ˆ instead of Python’s choice of **
will make these exercises easier because an operator will always be a single
character
"""

OPERATOR_PLUS_AND_MINUS = ['+', '-']
OPERATOR_MULTIPLE_AND_DIVISION = ['*', '/']
OPERATOR_SUPER_MULTIPLY = ['^']


def precedence(string_from_user: str) -> int:
    """Return 1 for operator '+' and '-'
        return 2 for operator '*' and '/'
        return 3 for operator '^'
    """

    for i in string_from_user:
        if i in OPERATOR_PLUS_AND_MINUS:
            return 1
        elif i in OPERATOR_MULTIPLE_AND_DIVISION:
            return 2 
        elif i in OPERATOR_SUPER_MULTIPLY:
            return 3 
    return -1


def get_string_from_user(message):
    string_from_user = input(message)
    return string_from_user


def main():
    message = 'Enter string with operator(s) -> '
    string_from_user = get_string_from_user(message)
    precedence_operator = precedence(string_from_user)
    print(precedence_operator)

if __name__ == '__main__':
    main()