#! /usr/bin/env python3 

""" 
TASK 
In this exercise, you will write a program to count
the average of all user-entered numbers. indicator
the end of the input will serve as zero. In this case, the program must issue
print an appropriate error message if the first typed
the user value will be zero.
"""

def get_user(msg: str = 'Enter number -> ') -> int:
    try:
        user_string = input(msg)
        number_user = int(user_string)
        return number_user
    except ValueError as err:
        print(f'You entered not valid number or string -> {err}')

def number_list_formation() -> list:
    list_numbers = []
    while True:
        list_numbers.append(get_user())
        if get_user() == 0:
            del(list_numbers[-1])
            break
        if list_numbers[0] == 0:
            del(list_numbers[0])
            break
    return list_numbers

def middle(numbers: list) -> float:
    average = sum(numbers) / len(numbers)
    
    return average

def main() -> None:
    numbers = number_list_formation()
    
    print(f'middle -> {middle(numbers):.2f}')
    
if __name__ == '__main__':
    main()
        