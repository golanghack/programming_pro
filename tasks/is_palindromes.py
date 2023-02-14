#! /usr/bin/env python3 

""" 
TASK
There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 75 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
further extend your solution so that is also ignores punctuation marks and treats
uppercase and lowercase letters as equivalent.
"""

import string 

strip_fmt = string.whitespace + string.punctuation + string.digits + "\"'"


def get_string(message: str) -> str:
    """Get string from user."""
    
    phrase = input(message)
    without_strip_phrase = phrase.lower()
    without_strip_phrase = without_strip_phrase.strip(strip_fmt)
    return without_strip_phrase

full_phrase = get_string('Enter phrase -> ')

def is_polidrom(line: str) -> bool:
    """Return boolean is polindrom."""
    
    for i in line:
        i_for_line = []
        i_for_line.append(i)
    for j in line[::-1]:
        j_for_line = []
        j_for_line.append(j) 
        
    if i_for_line != j_for_line:
        return False
    return True

def main() -> None:
    print(is_polidrom(full_phrase))
    
if __name__ == '__main__':
    main()