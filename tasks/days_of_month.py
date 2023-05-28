#! /usr/bin/env python3 

""" 
TASK 

Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month
""" 

from util_for_tasks.get_year import get_year
from util_for_tasks.get_number import get_number

DAYS_AND_MONTHS_STANDART_YEAR = {'0': 31, '1': 28, '2': 31, '3': 30, 
                                '4': 31, '5': 31, '6': 31, '7': 31,
                                '8': 31, '9': 30, '10': 31, '12': 31}
DAYS_AND_MONTHS_LEAP_YEAR = {'0': 31, '1': 29, '2': 31, '3': 30, 
                                '4': 31, '5': 31, '6': 31, '7': 31,
                                '8': 31, '9': 30, '10': 31, '12': 31}

def is_leap(year: int) -> bool:
    """Return boolean mean for year"""

    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return True
    return False


def main():
    MESSAGE_FOR_MONTH_NUMBER = 'Enter number of month -> '
    MESSAGE_FOR_YEAR_NUMBER = 'Enter year (from 1000 to 2050) -> '
    month_from_user = get_number(MESSAGE_FOR_MONTH_NUMBER)
    year_from_user = get_year(MESSAGE_FOR_YEAR_NUMBER)

    if is_leap(year_from_user):
        print(f'You entered month -> {month_from_user}')
        print(f'You entered year -> {year_from_user}')
        print(f'{DAYS_AND_MONTHS_LEAP_YEAR[str(month_from_user)]} days')
    else:
        print(f'You entered month -> {month_from_user}')
        print(f'You entered year -> {year_from_user}')
        print(f'{DAYS_AND_MONTHS_STANDART_YEAR[str(month_from_user)]} days')


if __name__ == '__main__':
    main()