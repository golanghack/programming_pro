#! /usr/bin/env python3 

def get_number(msg: str) -> int:
    """Return number got from user"""
    
    try:
        line = input(msg)
        line_number = int(line)
        return line_number
    except ValueError as err:
        print(f'You entered uncorrect number -> {err}')
        get_number(msg) 
        
