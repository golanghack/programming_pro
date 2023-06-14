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


def get_steps_and_validations(message: str) -> int:
    """Return number for steps""" 

    steps = get_number(message)
    if steps < 4:
       print(ValueError('Enter uncorrected steps! Try again'))
    return steps 


def get_list_number_from_user(message: str, steps: int) -> list:
    """return list numbers from user""" 
    
    stepper = True
    start = []
    while stepper:
        start.append(get_number(message))
        if len(start) == steps:
            stepper = False
    return start



