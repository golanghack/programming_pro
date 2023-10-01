#! /usr/bin/env python3 

"""TASK TEXT
Напишите программу, которая выводит сумму двух целых чисел.

Входные данные
В первой строке входных данных содержится целое число t (1≤t≤10**4) — количество 
наборов входных данных в тесте.
Далее следуют описания t наборов входных данных, один набор в строке.
В первой (и единственной) строке набора записаны два целых числа a и b (−1000≤a,b≤1000).

Выходные данные
Для каждого набора входных данных выведите сумму двух заданных чисел, то есть a+b.
"""

from random import choice

list_one_number: list = [number_one for number_one in range(1, 10001)]
list_two_number: list = [number_two for number_two in range(1, 10001)]

random_one_number: int = choice(list_one_number)
random_two_number: int = choice(list_two_number)

def summ_two_numbers(a: int, b: int) -> int:
    return a + b

summ_numbers = summ_two_numbers(random_one_number, random_two_number)

print(summ_numbers)