#! /usr/bin/env python3 

"""<--FROM USA GALLON ON MILES TO CANADIAN LITERS ON KM-->

В США потребление автомобильного топлива исчисляется в милях на
галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель
обычно выражается в литрах на 100 км (liters-per-hundred kilometers –
L/100 km). Используйте свои исследовательские способности, чтобы опре-
делить формулу перевода первых единиц исчисления в последние. После
этого напишите программу, запрашивающую у пользователя показатель
потребления топлива автомобилем в американских единицах и выводя-
щую его на экран в канадских единицах.

"""

ONE_GALLON_IN_LITR: float = 3.78541 #liters
ONE_MILE_IN_KM: float = 1.60934#km
MESSAGE: str = 'Enter USA parameters miles per gallon -> '
STANDART_DISTANCE: int = 100

try:
    line_miles = int(input(MESSAGE))
    
    line_miles_to_km:float = line_miles * ONE_MILE_IN_KM
    to_full_distance:float = STANDART_DISTANCE // line_miles_to_km
    
    full_value_liters:float = ONE_GALLON_IN_LITR * to_full_distance
    
    full_valume_disel:float = full_value_liters + ONE_GALLON_IN_LITR
    
    print(f'From USA {line_miles} to Canadian -> {full_valume_disel:.2f} liters per {STANDART_DISTANCE}km')
except ValueError as err:
    print(f'ERROR -> {err}. Try again')
    
    
    
    
    
    



