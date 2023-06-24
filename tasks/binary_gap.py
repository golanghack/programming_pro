#! /usr/bin/env python3 

""" 
TASK 

BinaryGap
VIEW START
Find longest sequence of zeros in binary representation of an integer.
"""


def find_zeros_in_numbers(numbers: list) -> int:
    """return list number with zero"""
    zero_numbers_list = []
    for number in numbers:
        zero = '0'
        string_number = str(number)
        if zero in string_number:
            zero_numbers_list.append(string_number)
    return zero_numbers_list


def longest_zeros_number(numbers: list) -> int:
    """find longest zero number in list"""

    list_len = []
    for number in numbers:
        len_number = len(number)
        list_len.append(len_number)
    max_zero_number = max(list_len)
    return max_zero_number

def main():
    start_numbers = [12, 20, 40, 400, 5000, 50000]
    numbers_list = find_zeros_in_numbers(start_numbers)
    longest = longest_zeros_number(numbers_list)
    print(start_numbers[longest])

if __name__ == '__main__':
    main()


