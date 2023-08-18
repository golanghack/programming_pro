#! /usr/bin/env python3 

""" 
TASK 
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determine whether or not it is a
palindrome. Display the result, including a meaningful output message.
"""

def get_string(message: str) -> str:
    """Get string from user."""
    
    line = input(message)
    return line

line = get_string('Enter string -> ')

def is_polidrom(line: str) -> bool:
    """Return boolean is polindrom."""
    
    for i in line:
        i_for_line = i 
    for j in line[::-1]:
        j_for_line = j 
        
    if i_for_line != j_for_line:
        return False
    return True

def main() -> None:
    print(is_polidrom(line))
    
if __name__ == '__main__':
    main()