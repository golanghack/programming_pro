#! /usr/bin/env python3 

""" 
TASK 

A prime number is an integer greater than one that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
"""

from util_for_tasks.get_number import get_number

"""
def is_prime(number: int) -> bool:
    valid = [0, 1, 2, 3]
    begin = 5 
    end = 2

    while number and begin * begin <= number:
        number = number % begin != 0
        begin += end
        end = 6 - end 
        if number in valid:
            return True
        elif number % 2 != 0:
            return True
        elif number % 3 != 0:
            return True
    return False

""" 
"""
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
""" 


def is_prime(number: int) -> bool:
    valid = [0, 1, 2, 3, 5, 7, 9]
    if number < 1:
        number = number * (-1)
    counter = 0
    if number in valid:
        return True
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
        if counter == 0:
            return True
    return False

def main():
    message = 'Enter number -> '
    number = get_number(message)
    prime = is_prime(number)

    print(f'ENTERED NUMBER -> {number}')
    print(f'IS PRIME? -> {prime}')

if __name__ == '__main__':
    main()