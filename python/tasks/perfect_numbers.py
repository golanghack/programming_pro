#! /usr/bin/env python3 

""" 
TASK 

An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your
function will return True. Otherwise it will return False. In addition, write a main
program that uses your function to identify and display all of the perfect numbers
between 1 and 10,000. Import your solution to Exercise 115 when completing this
task.
""" 

from typing import List

def self_delimeter(number: int) -> List[int]:
    """ 
    return list of self delimeter for number
    """
    delimeters_list = []
    for i in range(1,number+1):
        if number % i == 0:
            delimeters_list.append(i)
    return delimeters_list[:-1]

def perfect(number: int) -> bool:
    """
    >>> number = 4
    >>> perfect(number)
    False
    >>> number = 28
    >>> perfect(number)
    True
    """ 

    list_numbers = self_delimeter(number)
    sum_list_numbers = sum(list_numbers)
    if sum_list_numbers != number:
        return False
    return True

if __name__ == '__main__':
    LIST_OF_NUMBERS = [number for number in range(1, 10001)]

    for i in LIST_OF_NUMBERS:
        print(perfect(i))

