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
from typing import List


def universal_number_plate(list_letters: List[str], 
                            list_numbers: List[int],
                            switcher_not_new: bool=True) -> str:
    """REturn number plate"""

    if switcher_not_new:
        step_letter = step_number = 3
        slice_letters = random.sample(list_letters, step_letter)
        slice_numbers = random.sample(list_numbers, step_number)

        result_string_letter = ''
        result_string_letter = result_string_letter.join(map(str, slice_letters))
        result_string_number = ''
        result_string_number = result_string_number.join(map(str, slice_numbers)) 

        result_string = result_string_letter + result_string_number
        return result_string

    step_number = 4
    step_letter = 3
    slice_letters = random.sample(list_letters, step_letter)
    slice_numbers = random.sample(list_numbers, step_number)

    result_string_letter = ''
    result_string_letter = result_string_letter.join(map(str, slice_letters))
    result_string_number = ''
    result_string_number = result_string_number.join(map(str, slice_numbers)) 

    result_string = result_string_number + result_string_letter
    return result_string



if __name__ == '__main__':
    LETTERS = [chr(i) for i in range(65, 123)]
    NUMBERS = [i for i in range(10)]

    variator = [
        universal_number_plate(LETTERS, NUMBERS),
        universal_number_plate(LETTERS, NUMBERS, False),
    ]

    choicing = random.choice(variator)
    message = ''
    if len(choicing) < 7:
        message = 'old'
    else: 
        message = 'new'

    print(f'{message} -> {choicing}')
