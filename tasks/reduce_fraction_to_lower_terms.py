#! /usr/bin/env python3 

"""  
TASK 

Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only parameters. The body of the function should
reduce the fraction to lowest terms and then return both the numerator and denom-
inator of the reduced fraction as its result. For example, if the parameters passed
to the function are 6 and 63 then the function should return 2 and 21. Include a
main program that allows the user to enter a numerator and denominator. Then your
program should display the reduced fraction.
""" 

from util_for_tasks.get_number import get_number
import math


def fractions(nominator: int, denominator: int) -> tuple:
    """Return maximum possible fraction reduce"""
    
    minimal_unit = math.gcd(nominator, denominator)
    return (nominator // minimal_unit, denominator // minimal_unit)
    
def main():
    nominator = get_number('Enter nominator -> ')
    denominator = get_number('Enter denominator -> ')

    print(fractions(nominator, denominator))

if __name__ == '__main__':
    main()