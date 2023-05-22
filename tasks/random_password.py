#! /usr/bin/env python3 

""" 
TASK 

Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file.
""" 

import random


def random_password():
    """Generated random password from ascii table.""" 

    ascii_table = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
    random_integer = [str(i) for i in range(10)]
    len_password = [7, 8, 9, 10]
    choice_len = random.choice(len_password)
    empty_string = ''
    password = []
    for _ in range(choice_len):
        password.append(random.choice(ascii_table))
        password.append(random.choice(random_integer))

    long_apssword = empty_string.join(password)
    short_password = long_apssword[:choice_len]
    return short_password

def main():
    generated = random_password()
    print(generated)


if __name__ == '__main__':
    main()
    
        

