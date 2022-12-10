#! /usr/bin/env python3 

""" 
Интернет-магазин занимается продажей различных сувениров и безде-
лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
грамму, запрашивающую у пользователя количество тех и других покупок,
после чего выведите на экран общий вес посылки.
"""

suvenir_weigth: int = 75
garbage_weight: int = 122

message: str = 'Enter count ' 
gar: str = 'garbage'
suv: str = 'suvenirs'

try:
    line_suvenir = input(message + suv + ' -> ')
    line_garbage = input(message + gar + ' -> ')
    
    number_suv: int = int(line_suvenir)
    number_gar : int = int(line_garbage)
    
    full_weight = (number_suv * suvenir_weigth) + (number_gar * garbage_weight)
    
    print(f'Full weight of postbox -> {full_weight} gramm or {full_weight / 1000} kg')
except ValueError as err:
    print(f'You make error -> {err}. Please try again use this program! Thks!')
