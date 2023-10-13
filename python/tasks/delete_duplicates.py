#! /usr/bin/env python3 

"""TASK 

n this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should dis-
play each word entered by the user exactly once. The words should be displayed in
the same order that they were first entered. For example, if the user enters:
first
second
first
third
second
then your program should display:
first
second
third
""" 

def get_user(message: str) -> list:
    """get from user strings and return list of strings""" 

    start_list = []
    breaker = True
    while breaker:
        valid_string_for_exit = ''
        user_string = input(message)
        if user_string != valid_string_for_exit:
            start_list.append(user_string)
        else:
            breaker = False
    return start_list

def delete_duplicate(list_user_strings: list) -> list:
    """return list without duplicates"""

    new_list = dict.fromkeys(list_user_strings)
    return list(new_list)

def main():
    my_list = get_user('Enter -> ')
    after_delete_duplacates = delete_duplicate(my_list)
    print(f'BEFORE -> {my_list}############ AFTER -> {after_delete_duplacates}')

if __name__ == '__main__':
    main()

