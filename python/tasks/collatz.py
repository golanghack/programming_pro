#! /usr/bin/env python3 

""" 
TASK 

Consider a sequence of integers that is constructed in the following manner:
Start with any positive integer as the only term in the sequence
While the last term in the sequence is not equal to 1 do
If the last term is even then
Add another term to the sequence by dividing the last term by 2 using
floor division
Else
Add another term to the sequence by multiplying the last term by 3 and
adding 1
The Collatz conjecture states that this sequence will eventually end with one when
it begins with any positive integer. Although this conjecture has never been proved,
it appears to be true.
Create a program that reads an integer, n, from the user and reports all of the
values in the sequence starting with n and ending with one. Your program should
allow the user to continue entering new n values (and your program should continue
displaying the sequences) until the user enters a value for n that is less than or equal
to zero
"""

import math
import sys  

def get_number(msg: str) -> int:
    """ 
    This function return get user data."""
    
    try:
        line = input(msg)
        number_from_line = int(line)
        if number_from_line == 0 or number_from_line < 0:
            sys.exit(1)
    except ValueError as err:
        print(f'You entered wrong mean. ERROR -> {err}. Try again.')
    return number_from_line

def collazt(end_list: list) -> list:
    """Seracuses (Collatz gipothese) frequences."""
    
    while end_list[-1] != 1:
        if end_list[-1] % 2 == 0:
            end_list.append(math.floor(end_list[-1] / 2))
        else:
            end_list.append((end_list[-1] * 3) + 1)
    return end_list
        
def main() -> None:
    message_to_user: str = 'Enter number (or 0 or -1 for exit) -> '
    
    while True:
        any_number = get_number(message_to_user)
        start_list = [i for i in range(1, any_number + 1)]
        print(collazt(start_list))
    
if __name__ == '__main__':
    main()
    
