#! /usr/bin/env python3

"""<--ROOM-->"""
"""<--TASK TEXT-->"""
""" 
Напишите программу, запрашивающую у пользователя длину и ширину
комнаты. После ввода значений должен быть произведен расчет площади
комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
в формате числа с плавающей запятой. Дополните ввод и вывод единицами
измерения, принятыми в вашей стране. Это могут быть футы или метры.
"""

try:
    message_for_lenght = 'Enter lenght wall in room as metr--> '
    message_for_width = 'Enter width wall in room as metr--> '
    
    int_lenght = float(input(message_for_lenght))
    int_width = float(input(message_for_width))
    
except TypeError as err:
    print(err)

if __name__ == '__main__':
    square = int_lenght * int_width
    print('Square room -> ',  square, ' meters')
