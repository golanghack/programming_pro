#! /usr/bin/env python3

""" 
Площадь треугольника может быть вычислена с использованием следую­
щей формулы, где b – длина основания треугольника, а h – его высота:
Напишите программу, в которой пользователь сможет вводить значе-
ния для переменных b и h, после чего на экране будет отображена площадь
треугольника с заявленными основанием и высотой.

area = (b * h) / 2.
"""

list_messages: list = ['Enter fundament of treangulum -> ', 
                       'Enter height of treangulum -> ',]
meas_system: str = 'sm'

try:
    string_fundament: str = input(list_messages[0])
    string_height: str = input(list_messages[1])  
        
    number_fundament: float = float(string_fundament)
    number_height: float = float(string_height)

except ValueError as err:
    print(f'!!!ERROR!!! -> {err}')
    print('Try again!')
    
def treangulum_area(fundament: float, height: float) -> float:
    """Traengulum area."""
    
    return (fundament * height) / 2

area_of_treangle = treangulum_area(number_fundament, number_height)
print(f'area_of_treangle -> {area_of_treangle:.2f} {meas_system}')
