#! /usr/bin/env python3 

"""
TASK 

Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""

from util_for_tasks.get_number import get_number

def main():

    a, b = get_catets(message_for_user)
    hyp = hypot(a, b)

    print(f'catet a -> {a}, catet b -> {b}')
    print()
    print(f'<--------> {hyp:.2f} <-------->')

message_for_user: str = 'Enter catet -> '

def get_catets(message_for_user):
    catet_a: int = get_number(message_for_user)
    catet_b: int = get_number(message_for_user)
    return catet_a, catet_b 

def hypot(a, b):
    hypothenuse = ((a ** 2) + (b ** 2)) ** 0.5
    return hypothenuse


if __name__ == '__main__':
    main()

