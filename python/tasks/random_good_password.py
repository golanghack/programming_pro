#! /usr/bin/env python3 

""" 
TASK 

Using your solutions to Exercises 100 and 102, write a program that generates a
random good password and displays it. Count and display the number of attempts
that were needed before a good password was generated. Structure your solution so
that it imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise.
""" 

from random_password import random_password
from check_a_password import *

def generator_password():
    password = random_password()
    return password

def perfect_password(password: str) -> bool:
    lower = get_lower_letter(password)
    upper = get_upper_letter(password)
    integer = get_integer_include(password)
    get_lenght = corect_lenght(password)
    
    condition = (lower == upper == integer == get_lenght)
    return condition

if __name__ == '__main__':
    counter = 1
    password = generator_password()
    perfect = perfect_password(password)
    if perfect != True:
        counter += 1

    print(f'trying -> {counter} -> and good password -> {password}')
    


