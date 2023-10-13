#! /usr/bin/env python3 

"""
TASK 

Create a function that takes an ordinal date, consisting of a year and a day within in
that year, as its parameters. The function will return the day and month correspond-
ing to that ordinal date as its results. Ensure that your function handles leap years
correctly.
Use your function, as well as the ordinalDate function that you wrote previ-
ously, to create a program that reads a date from the user. Then your program should
report a second date that occurs some number of days later. For example, your pro-
gram could read the date a product was purchased and then report the last date that
it can be returned (based on a return period that is a particular number of days), or
your program could compute the due date for a baby based on a gestation period of
280 days. Ensure that your program correctly handles cases where the entered date
and the computed date occur in different years
"""

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

LIST_ON_MONTHS = ['Jan', 'Feb', 'March', 'Apr', 'May', 'Jun', 'Jul', 
                    'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

BIRTH = 280
RETURN_RULES = 90


def leap_year(year: int) -> int:
    """Test year for leap."""
    days_in_year = 365
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 1 + days_in_year
    return days_in_year

def from_user():
    year = get_number('Enter year -> ')

    number_of_day = get_number('Enter number for start day ->  from 1 to 366')
    if number_of_day > 366 or number_of_day < 1:
        raise ValueError('You entered uncorrect date. Try Again')
    return year, number_of_day

year, number_of_day = from_user()

        

