#! /usr/bin/env python3 

"""<--BMI-->

Напишите программу для расчета индекса массы тела (body mass index –
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы
используете одну из приведенных ниже формул для определения индекса.
Если пользователь вводит рост в дюймах, а вес в фунтах, формула будет
следующей:

 --> BMI = (weight / height**2) * 703
 
Если же пользователь предпочитает вводить информацию о себе в сан-
тиметрах и килограммах, формула упростится и станет такой:

--> BMI = weight / height**2
"""


get_switcher_message: str = 'Enter for metric system - > "m" or "f" for funts metric system -> '
get_height_message: str = 'Enter your height --> '
get_weight_message: str = 'Enter your weight --> '

try:
    switcher_funt_metr = input(get_switcher_message)
    line_height: str = input(get_height_message)
    line_weight: str = input(get_weight_message)
    
    height: float = float(line_height)
    weight: float = float(line_weight)
    
    if switcher_funt_metr == 'f':
        body_mass_index = (weight / (height ** 2)) * 703
        print(f'Your BMI -> {body_mass_index}')
    if switcher_funt_metr == 'm':
        body_mass_index = weight / (height ** 2)
        print(f'Your BMI -> {body_mass_index}')
except ValueError as err:
    print(f'Your error -> {err}. Try again!')
