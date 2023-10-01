#! /usr/bin/env python3 

import random


def get_number(msg: str) -> int:
    """Return number got from user"""
    
    try:
        line = input(msg)
        line_number = int(line)
        if line_number >= 1 and line_number <= 100:
            return line_number
        print('You enter uncorrect number (from 1 to 100). Try again.')
        return get_number(msg)
    except ValueError as err:
        print(f'You entered uncorrect number -> {err}')
        get_number(msg) 


n_rows = get_number('Enter rows in fly(from 1 to 100) -> ')
m_cols = get_number('Enter cols in fly(from 1 to 100) -> ')

pass_count = [1, 2, 3]

num = random.choice(pass_count)
sides = ['left', 'right',]
position = ['aisle', 'window',]
