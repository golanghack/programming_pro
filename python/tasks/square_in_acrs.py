#! /usr/bin/env python3 

"""<--SQUARE IN ACRS-->"""
"""<--TASK-->"""
"""
Создайте программу, запрашивающую у пользователя длину и ширину
садового участка в футах. Выведите на экран площадь участка в акрах.
Подсказка. В одном акре содержится 43 560 квадратных футов.
"""

message_for_lenght = 'Enter lenght --> '
message_for_width = 'Enter widht --> '

try:
    lenght = int(input(message_for_lenght))
    width = int(input(message_for_width))
    
except TypeError as err:
    print(err)
    
square_in_acrs = (lenght * width) * 43560 

if __name__ == '__main__':
    print(square_in_acrs, ' acrs.')
     