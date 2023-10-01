#! /usr/bin/env python3 

""" 
Напишите программу, запрашивающую у пользователя число и подсчи-
тывающую сумму натуральных положительных чисел от 1 до введенного
пользователем значения. Сумма первых n положительных чисел может
быть рассчитана по формуле:
sum = ((n)(n + 1))/2
"""

message: str = 'enter number -> '
try:
    line = input(message)
    number = int(line)
    
    summ = int(((number) * (number + 1)) / 2)
    
    print(f'You entered -> {number} and get -> {summ}')
except ValueError as err:
    print(f'!!!ERROR!!! {err} try again!')

