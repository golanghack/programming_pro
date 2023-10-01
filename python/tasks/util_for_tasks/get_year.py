#! /usr/bin/env python3 

def get_year(msg: str) -> int:
    """Return year on len 4 integers"""
    
    try:
        line = input(msg)
        if len(line) != 4:
            raise ValueError
        line_number = int(line)
        if line_number >= 1000 and line_number <= 2050:
            return line_number
        raise ValueError
    except ValueError as err:
        print(f'You entered uncorrect number -> {err}')
        get_year(msg) 
    