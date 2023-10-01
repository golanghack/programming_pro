#! /usr/bin/env python3 

def get_number(msg: str) -> int:
    """From user number."""

    try:
        line = input(msg)
        line_number = int(line)
        return line_number
    except ValueError as err:
        print(f'You entered uncorrect number -> {err}')
        get_number(msg) 
        

def is_valid(number: int, list_numbers: list) -> bool:
    """Testing number contains in list."""

    if number in list_numbers:
        return True
    return False

def main():
    message = 'Enter number -> '
    number = get_number(message)
    list_numbers = [i for i in range(100)]

    if is_valid(number, list_numbers) == True:
        print('Bingo!')
    else:
        print('Zero!')


if __name__ == '__main__':
    main()