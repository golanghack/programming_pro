#! /usr/bin/env python3 

"""<--ARIPHMETIC-->

Создайте программу, которая запрашивает у пользователя два целых чис-
ла a и b, после чего выводит на экран результаты следующих математи-
ческих операций:
  сумма a и b;
  разница между a и b;
  произведение a и b;
  частное от деления a на b;
  остаток от деления a на b;
  десятичный логарифм числа a;
  результат возведения числа a в степень b.
"""

import math

MESSAGE: str = 'Enter number from 0 to 100 -> '

try: 
    line_a = input(MESSAGE)
    line_b = input(MESSAGE)
    
    number_a = int(line_a)
    number_b = int(line_b)
    
    summ = number_a + number_b
    diff = number_a - number_b
    
    reverse_diff = number_b - number_a
    mul = number_a * number_b
    
    divide_first_on_second = number_a // number_b
    divide_secodn_on_first = number_b // number_a
    
    piece = number_a % number_b
     
    logariphm = math.log10(number_a)
    
    pow_a_in_b = number_a ** number_b
     
except ValueError as err:
    print(f'ERROR -> {err} -> Try again!')
    

def print_results():
    """Printing results"""
    
    fill = '********'
    
    print(fill + f'summ -> {summ}' + fill)
    print(fill + f'diff -> {diff}' + fill)
    print(fill + f'reverse diff -> {reverse_diff}' + fill)
    print(fill + f'mul -> {mul}' + fill)
    print(fill + f'divide first on second number -> {divide_first_on_second}' + fill)
    print(fill + f'piece -> {piece}' + fill)
    print(fill + f'logariphm -> {logariphm}' + fill)
    print(fill + f'pow a number in b number -> {pow_a_in_b}' + fill)
    
if __name__ == '__main__':
    print_results()