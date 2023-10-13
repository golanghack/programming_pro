#! /usr/bin/env python3 

""" 
TASK 

Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers.
The hex2int function is responsible for converting a string containing a single
hexadecimal digit to a base 10 integer, while the int2hex function is responsible
for converting an integer between 0 and 15 to a single hexadecimal digit. Each
function will take the value to convert as its only parameter and return the converted
value as its only result. Ensure that the hex2int function works correctly for both
uppercase and lowercase letters. Your functions should display a meaningful error
message and end the program if the parameter’s value is outside of the expected
range.
""" 


HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
DECIMAL = [str(i) for i in range(15)]
LEN_MINIMAL_LEN_MAXIMAL = 1

message_to_hex = 'Enter hex number -> '
message_to_decimal = 'Enter decimal number -> '

def get_number(msg: str) -> int:
    """Return number got from user"""
    line_number = input(msg)
    return line_number 
        

def work_with_user_hex(message_to_hex):
    get_user_hex = get_number(message_to_hex)
    get_user_hex = get_user_hex
    return get_user_hex

def work_with_user_decimal(message_to_decimal):
    get_user_decimal = get_number(message_to_decimal)
    return get_user_decimal

def hex_to_int(get_user_hex: str) -> int:

    index_in_list_hex_numbers = HEX.index(get_user_hex.upper())
    index_int_in_list_decimal_numbers = DECIMAL[index_in_list_hex_numbers]
    return index_int_in_list_decimal_numbers

def int_to_hex(get_user_decimal: str):
    index_int_in_list_decimal_numbers = DECIMAL.index(get_user_decimal)
    index_in_list_hex_numbers = HEX[index_int_in_list_decimal_numbers]
    return index_in_list_hex_numbers


if __name__ == '__main__':
    get_user_hex = work_with_user_decimal(message_to_decimal)
    get_user_decimal = work_with_user_hex(message_to_hex)

    hex2int = hex_to_int(get_user_hex)
    int2hex = int_to_hex(get_user_decimal)

    print(f'You entered -> HEX {get_user_hex} -> INT {hex2int}')
    print(f'You entered -> INT {get_user_decimal} -> HEX {int2hex}')
    
        





    




        