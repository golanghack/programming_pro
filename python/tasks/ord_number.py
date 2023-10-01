#! /usr/bin/env python3 

"""TEXT TASK
Напишите программу, которая выводит чётные числа из заданного списка 
и останавливается, если встречает число 237
"""


get_numbers: list = [1, 2, 3, 4, 5, 6, 237, 45, 43, 44]
for num in get_numbers:
    if num % 2 == 0:
        print(num)
    if num == 237:
        break

