#! /usr/bin/env python3 

"""
TASK 

In this exercise you will write a function named isInteger that determines
whether or not the characters in a string represent a valid integer. When deter-
mining if a string represents an integer you should ignore any leading or trailing
white space. Once this white space is ignored, a string represents an integer if its
length is at least one and it only contains digits, or if its first character is either +
or - and the first character is followed by one or more characters, all of which are
digits.
Write a main program that reads a string from the user and reports whether or
not it represents an integer. Ensure that the main program will not run if the file
containing your solution is imported into another program.
Hint: You may find the lstrip, rstrip and/or strip methods for strings
helpful when completing this exercise. Documentation for these methods is
available online.
"""

def get_string(message: str) -> str:
    line = input(message)
    return line

def validation(line: str) -> int:
    """Return number got from user"""
    
    try:
        if line[0] == '+' or line[0] == '-':
            line = line[1:]
        line_number = int(line)
        return line_number
    except ValueError as err:
        print(f'You entered uncorrect number -> {err}')

def is_integer(line: str) -> bool:
    return isinstance(line, int)

def main():
    line = get_string('Enter string ->')
    valid = validation(line)
    print(is_integer(valid))

if __name__ == '__main__':
    main()
    