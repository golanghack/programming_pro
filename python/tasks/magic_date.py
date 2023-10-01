#! /usr/bin/env python3 

""" 
TASK 

A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century.
""" 

from util_for_tasks.get_year import get_year
from util_for_tasks.get_number import get_number

DAYS_AND_MONTHS_STANDART_YEAR = {'0': 31, '1': 28, '2': 31, '3': 30, 
                                '4': 31, '5': 31, '6': 31, '7': 31,
                                '8': 31, '9': 30, '10': 31, '12': 31}
DAYS_AND_MONTHS_LEAP_YEAR = {'0': 31, '1': 29, '2': 31, '3': 30, 
                                '4': 31, '5': 31, '6': 31, '7': 31,
                                '8': 31, '9': 30, '10': 31, '12': 31}
FROM_MONTHS_STR_TO_INT = {'jan': 1, 'feb': 2, 'march': 3, 
                            'apr': 4, 'may': 5, 'jun': 6,
                            'jul': 7, 'aug': 8, 'sep': 9, 
                            'oct': 10, 'nov': 11, 'dec': 12}

def is_leap(year: int) -> bool:
    """Return boolean mean for year"""

    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return True
    return False

def date_from_string_to_list(date: str) -> list:
    """Return parsing string to list""" 

    # parse of date
    list_of_date_string = date.split()

    day = list_of_date_string[0]
    month = list_of_date_string[1]
    year = list_of_date_string[2]

    result = [day, month, year]
    return result

def recombination_from_string_to_int(data: str) -> int:
    """recombination from string to integer for months""" 

    month = data[1]
    if month not in FROM_MONTHS_STR_TO_INT:
        raise ValueError('Enter correct months name')
    else:
        return FROM_MONTHS_STR_TO_INT[month]

def validation_data(data:list) -> bool:
    """Return True if data validation""" 

    if int(data[0]) > 31 or int(data[1]) > 12 or int(data[2]) > 2000:
        return False
    
    return True


def parse_ended_year(data: int) -> int:
    """return end two unit from year"""

    return data[2:]

def is_magic(data: list) -> bool:
    """Return magic or not megic for True and False""" 

    if (int(data[0]) * int(data[1])) == int(data[2]):
        return True
    return False

 