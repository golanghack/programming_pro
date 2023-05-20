#! /usr/bin/env python3 

""" 
TASK 

In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters long
and contains at least one uppercase letter, at least one lowercase letter, and at least
one number. Your function should return True if the password passed to it as its
only parameter is good. Otherwise it should return False. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.
""" 

SAFE_LENGHT = 8 
SAFE_UPPER_LETTER = [chr(upper_letter) for upper_letter in range(65, 91)]
SAFE_LOWER_LETTER = [chr(lower_letter) for lower_letter in range(97, 123)]
SAFE_INTEGER = [str(integer) for integer in range(10)]
MESSAGE = 'Enter password -> '

def get_string_from_user(message: str) -> str:
    password = input(message)
    return password


def get_lower_letter(password: str) -> bool:
    for low in password:
        if low in SAFE_LOWER_LETTER:
            return True
        else:
            return False

def get_upper_letter(password: str) -> bool:
    for up in password:
        if up in SAFE_UPPER_LETTER:
            return True
        else:
            return False


def get_integer_include(password: str) -> bool:
    for i in password:
        if i in SAFE_INTEGER:
            return True
    return False

def is_good_password(password) -> bool:
    is_good = (get_integer_include(password) == get_lower_letter(password) == get_upper_letter(password))
    return is_good

    
if __name__ == '__main__':
    password = get_string_from_user(MESSAGE)
    verdict = is_good_password(password)
    print(f'You entered password -> {password} and this -> {verdict}')
