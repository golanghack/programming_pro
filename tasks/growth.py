#! /usr/bin/env python3 
"""<--GROWTH-->

Task

Многие люди на планете привыкли рассчитывать рост человека в футах
и дюймах, даже если в их стране принята метрическая система. Напишите
программу, которая будет запрашивать у пользователя количество футов,
а затем дюймов в его росте. После этого она должна пересчитать рост
в сантиметры и вывести его на экран.
Подсказка. Один фут равен 12 дюймам, а один дюйм – 2,54 см.
"""

one_fit_in_duims = 12
one_duim_in_sm = 2.54

try:
    
    message_fit = 'Enter you grow fit -> '
    message_duim = 'Enter you grow duim -> '
    
    fits = float(input(message_fit))
    duims = float(input(message_duim))
    
    from_fits_to_duims = fits * one_fit_in_duims
    
    full_grow_in_duims = duims + from_fits_to_duims
    
    full_grow_in_sm = full_grow_in_duims * one_duim_in_sm
    
    print(f'Your grow -> {full_grow_in_sm:.0f} sm')
except ValueError as err:
    print(f'!!!ERRORR!!! You entered dont supported date! Try again! Error -> {err}')
    

