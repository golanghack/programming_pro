#! /usr/bin/env python3 

"""TASK 
   
   An ordinal date consists of a year and a day within it, both of which are integers. The
year can be any year in the Gregorian calendar while the day within the year ranges
from one, which represents January 1, through to 365 (or 366 if the year is a leap
year) which represents December 31. Ordinal dates are convenient when computing
differences between dates that are a specific number of days (rather than months). For
example, ordinal dates can be used to easily determine whether a customer is within
a 90 day return period, the sell-by date for a food-product based on its production
date, and the due date for a baby.
Write a function named ordinalDate that takes three integers as parameters.
These parameters will be a day, month and year respectively. The function should
return the day within the year for that date as its only result. Create a main program
that reads a day, month and year from the user and displays the day within the year for
that date. Your main program should only run when your file has not been imported
into another program.
"""

from functools import wraps
from util_for_tasks.get_number import get_number

MONTHS = {
    '1': 0, 
    '2': 31, 
    '3': 59,
    '4': 90, 
    '5': 120,
    '6': 151, 
    '7': 182, 
    '8': 213, 
    '9': 244,
    '10': 275, 
    '11': 306, 
    '12': 335
}

def from_user():
    """This function get number for day, month and yer from user."""

    day = get_number('Enter number of day from 1 to 366 -> ')
    if (day < 1) or (day > 366):
        raise ValueError('Non correct day number.Try Again.')

    month = get_number('Enter number of month from 1 to 12 -> ')
    if (month > 12) or (month < 1):
        raise ValueError('Non correct month number.Try Again')

    year = get_number('Enter year in grigorean calendar.')
    return day, month, year

def leap_year(year: int) -> int:
    """Test year for leap."""
    days_in_feb = MONTHS['1']
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 1 + days_in_feb
    return 0 + days_in_feb


def ordinal_date() -> int:
    """Return ordered day in this year."""

    day, month, year = from_user()
    year = leap_year(year)
    month = str(month)

    order = day + MONTHS[month]
    print(f'<--{order}-->')

def main():
    ordinal_date()

if __name__ == '__main__':
    main()







