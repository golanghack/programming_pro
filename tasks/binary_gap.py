#! /usr/bin/env python3 

""" 
TASK 

BinaryGap
VIEW START
Find longest sequence of zeros in binary representation of an integer.
"""

def to_binary(number: int):
    """return list binary integers""" 
    return bin(number)


def find_longest_indent_with_zeros(N: int) -> int:
    """return longest indent with zeros"""

    bin_num = bin(N)
    bad_pattern = '0b'
    if bad_pattern in bin_num:
        bin_num = bin_num.replace(bad_pattern, '')
    string_num = str(bin_num)
    splitting_num = string_num.split('1')
    binary_indent = str(splitting_num)
    have_a_binary_undent = True
    bin_split = binary_indent.split('0')
    
    if '' in bin_split:
        have_a_binary_undent = False
    lens_num = []
    for line in splitting_num:
        lens_num.append(len(line))
    if have_a_binary_undent == True or string_num[-1] != '0':
        return max(lens_num)
    else:
        return 0

print(find_longest_indent_with_zeros(32))


        






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
    """start = [12, 20, 40, 400, 5000, 50000]
    start_numbers = to_binary(start)
    numbers_list = find_zeros_in_numbers(start_numbers)
    longest = longest_zeros_number(numbers_list)
    print(start_numbers[longest])"""

if __name__ == '__main__':
    main()


