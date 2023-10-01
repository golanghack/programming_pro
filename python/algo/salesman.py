#! /usr/bin/env python3 

"""salesman"""

import math 
import numpy as np
import matplotlib.collections as mc
import matplotlib.pylab as pl 

"""<--GENERATING CARD for salesman-->"""
random__variation = 1729
np.random.seed(random__variation)
#count of cities
N = 40
x = np.random.rand(N)
y = np.random.rand(N)

#coords
points = zip(x, y)
cities = list(points)

#ordering moving for salesman
points_visit_for_salesman = list(range(0, N))

#generator for distances between cities
def generator_distance(cities: list, points_visit_for_salesman: list) -> list:
    lines: list = []
    for i in range(0, len(points_visit_for_salesman) - 1):
        lines.append([cities[points_visit_for_salesman[i]], cities[points_visit_for_salesman[i + 1]]])
    return lines

def unit_distance(lines: list) -> float:
    """Unit distance between cities"""
    
    distance = 0
    for i in range(0, len(lines)):
        #Piphagor teorem for distance
        distance += math.sqrt(abs(lines[i][1][0] - lines[i][0][0]) ** 2 + 
                              abs(lines[i][1][1] - lines[i][0][1]) ** 2)
    return distance

#total distance for salesman for all cities
all_cities_distance = unit_distance(generator_distance(cities, points_visit_for_salesman))

#drowning point and distanc between cities and lines 
def draw(cities: list, order_map: int, title: str, out_name: str) -> None:
    """Generate picture for format png 
    cities - list of cities(points), 
    order_map - int -> counting oreds for travaling salesman
    title -> diagram name
    out_name -> str -> name of png picture
    """
    
    lc = mc.LineCollection(generator_distance(cities, points_visit_for_salesman), linewidths=3)
    figure, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.2)
    pl.scatter(x, y)
    pl.title(title)
    pl.xlabel('X Coord')
    pl.ylabel('Y Coord')
    pl.savefig(str(out_name) + '.png')
    pl.close()
    
    
    
draw(cities, generator_distance, 'TSP -Random', 'Picture1')


