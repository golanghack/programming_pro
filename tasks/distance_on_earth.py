#! /usr/bin/env python3

"""<--DISTANCE ON EARTH--> 

TASK

Как известно, поверхность планеты Земля искривлена, и расстояние меж-
ду точками, характеризующимися одинаковыми градусами по долготе,
может быть разным в зависимости от широты. Таким образом, для вычис
ления расстояния между двумя точками на Земле одной лишь теоремой
Пифагора не обойтись.
Допустим, (t 1 , g 1 ) и (t 2 , g 2 ) – координаты широты и долготы двух точек на
поверхности Земли. Тогда расстояние в километрах между ними с учетом
искривленности планеты можно найти по следующей формуле:
distance = 6371,01 ́arccos(sin(t 1 ) ́sin(t 2 ) + cos(t 1 ) ́cos(t 2 ) ́cos(g 1 - g 2 )).

Примечание. Число 6371,01 в этой формуле, конечно, было выбрано не случайно
и представляет собой среднее значение радиуса Земли в километрах.

Напишите программу, в которой пользователь будет вводить коорди-
наты двух точек на Земле (широту и долготу) в градусах. На выходе мы
должны получить расстояние между этими точками при следовании по
кратчайшему пути по поверхности планеты.

Подсказка. Тригонометрические функции в Python оперируют радианами. Таким
образом, вам придется введенные пользователем величины из градусов перевести
в радианы, прежде чем вычислять расстояние между точками. В модуле math есть
удобная функция с названием radians-Функции:radians, служащая как раз для пере-
вода градусов в радианы.
"""

import math 

RADIUS = 6371.01

def get_coords() -> float:
    """Geti coords from user"""
    
    message_latitude = 'Enter coords in grad - latitude -> '
    message_longitude = 'Enter coords in grad -> longitude -> '

    try: 
        line_latitude = input(message_latitude)
        line_longitude = input(message_longitude)
    
        int_latitude = float(line_latitude)
        int_longitude = float(line_longitude)
    except ValueError as err:
        print(f'!!!ERROR!!! -> {err}. Try Again!')
    return (int_latitude, int_longitude)

    
def converter_grad_to_radians(latitude: float, longitude: float) -> float:
    """Convartion graduses in radians"""
    
    rad_latitude = math.radians(latitude)
    rad_longitude = math.radians(longitude)
    
    return (rad_latitude, rad_longitude)

def distance(lat1: float, lat2: float, long1: float, long2: float) -> float:
    """Find distance between two point with coords -> (lat1, long1) and (lat2, long2)"""
    
    return RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2))


def main():
    get_lat1, get_long1  = get_coords()
    get_lat2, get_long2 = get_coords()
    
    lat1, long1 = converter_grad_to_radians(get_lat1, get_long1)
    lat2, long2 = converter_grad_to_radians(get_lat2, get_long2)
    
    
    distance_between = distance(lat1, lat2, long1, long2)
    
    print(f'distance from {lat1:.3f}, {long1:.3f} to {lat2:.3f}, {long2:.3f} -> {distance_between:.3f} km')
    

if __name__ == '__main__':
    main()
    
    
    
    
    