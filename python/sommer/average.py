#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--AVERAGE-->"""

"""Напишите программу, которая в цикле while предлагала бы пользователю ввести
число, постепенно накапливая список введенных чисел. Затем, кoгда пользователь 
завершит работу с программой (простым нажати
ем клавиши Enter), она выводила бы числа, введенные пользовате
лем, количество введенных чисел, их сумму, наименьшее и наи
большее число и среднее значение (сумма / количество). Ниже при
водится пример сеанса работы с программой:
average1_ans.py
enter a number or Enter to finish: 5
enter a number or Enter to finish: 4
enter a number or Enter to finish: 1
enter a number or Enter to finish: 8
enter a number or Enter to finish: 5
enter a number or Enter to finish: 2
enter a number or Enter to finish:
numbers: [5, 4, 1, 8, 5, 2]
count = 6 sum = 25 lowest = 1 highest = 8 mean = 4.16666666667.
"""
start_list = []

while True:
    try:
        line = input('Enter number --> ')
        if not line:
            break
        number = int(line)
        start_list.append(number)
    except ValueError as err:
        print(err)
    except IOError:
        break

numbers = start_list
count = len(start_list)
lowest = min(numbers)
highest = max(numbers)
mean = sum(numbers)/len(numbers)

print(f'''numbers --> {numbers}, 
      count --> {count},
      lowest --> {lowest}, 
      highest --> {highest},
      mean --> {mean} ''')