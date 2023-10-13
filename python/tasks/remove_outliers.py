#! /usr/bin/env python3 

""" 
TASK 

When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.
Write a main program that demonstrates your function. It should read a list of
numbers from the user and remove the two largest and two smallest values from it by
calling the function described previously. Display the list with the outliers removed,
followed by the original list. Your program should generate an appropriate error
message if the user enters less than 4 values.
"""
from util_for_tasks.get_number import get_number

STANDART_MIDDLE_COEFFICIENT = 2

def mediane(list_user_numbers: list) -> float:
    return sum(list_user_numbers) // len(list_user_numbers)


def shorter_max_min(list_user_numbers: list, median) -> list:
    max_coefficient = median * STANDART_MIDDLE_COEFFICIENT
    min_coefficient = median // STANDART_MIDDLE_COEFFICIENT

    for number in list_user_numbers:
        if number >= max_coefficient and number <= min_coefficient:
            n_list = list_user_numbers.remove(number)
    return n_list

def main():
    switcher = 0
    list_user_numbers = []
    while switcher < 10:
    
        list_user_numbers.append(get_number('Enter number -> '))
        switcher += 1

    median = mediane(list_user_numbers)
    new_list = shorter_max_min(list_user_numbers, median)
    print(f'After -> {new_list}')
    print(f'Before -> {list_user_numbers}')
        

if __name__ == '__main__':
    main()