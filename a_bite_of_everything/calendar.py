#! /usr/bin/env python3 

from datetime import date
import calendar

lenght_month_in_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
names_of_months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'Jule', 'Aug',
                            'Sep', 'Oct', 'Nov', 'Dec']

def is_leap(year: int) -> bool:
    if ((year % 400 == 0) and (year % 100 == 0)):
        return True
    return False


def build_month(month: str, year: int) -> str:
    """Return name of month and counting day in month as a table""" 

    index_month = names_of_months.index(month)
    weekday_out = date(year, index_month + 1, 1).weekday()
    days = lenght_month_in_days[index_month]

    if is_leap(year) and index_month == 1:
        days = days + 1
    return (weekday_out, days)

def get_year(message: str='Enter year -> ') -> int:
    try:       
        line = input(message)
        number = int(line)
    except TypeError as err:
        print(f'Enter error-> {err}')
        print('Try again -> ')
        get_year() 
    return number

def get_month(message: str='Enter name of month -> '):
    month = input(message)
    return month 

def main():
    month = get_month()
    year = get_year()
    weekday_out, days = build_month(month, year)

    print(f'{month} {year}'.center(20))
    print('Mon Tru Wed Trs Fri Sat Sun')
    print('    ' * weekday_out, end='')

    for day in range(days):
        weekday_out = (weekday_out + 1) % 7
        eow = ' ' if weekday_out %7 else '\n'
        print(f'{day+1:2}', end=eow)
    print()

if __name__ == '__main__':
    main()