#! /usr/bin/env python3 

""" 
TASK 

In a particular jurisdiction, older license plates consist of three letters followed by
three digits. When all of the license plates following that pattern had been used, the
format was changed to four digits followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
"""

import random


def universal_number_plate(list_letters: list, 
                            list_numbers: list, 
                            len_numbers: int, 
                            len_letters: int, 
                            switcher: bool=True) -> str:
    """Return plate in old format.""" 

    
    if switcher:
        for i in range(3):
            letter = random.choice(list_letters)
            number = random.choice(list_numbers)
            numbers = []
            numbers = numbers.append(number)
            letters = []
            letters = letters.append(letter)
        return str(letters) + str(numbers)  

    for i in range(4):
        number = random.choice(list_numbers)
        numbers = []
        numbers = numbers.append(number)
    
    for j in range(3):
        letter = random.choice(list_letters)
        letters = []
        letters = letters.append(letter)

    return str(numbers) + str(letters)


if __name__ == '__main__':

    LETTERS = [chr(i) for i in range(65, 123)]
    OLD_NUMBERS = [i for i in range(1000)]
    NEW_NUMBERS = [i for i in range (1000, 10000)]
    
    variator = [
        universal_number_plate(LETTERS, OLD_NUMBERS, 3, 3),

        universal_number_plate(LETTERS, NEW_NUMBERS, 4, 3, False)
    ]

    random_plate = random.choice(variator)

    print(f'Random number plate -> {random_plate}')


