#! /usr/bin/env python3 

"""<--GEOMETRY-->"""

import math
import pylab as pl 
from matplotlib import collections as mc 

point: list = [0.8, 0.2]
triangle_simple: list = [[0.8, 0.2], [0.5, 0.2], [0.6, 0.7]]

def from_points_to_triangle(point1: list, point2: list, point3: list) -> list:
    """Building triangle from three points"""
    
    triangle = [list(point1), list(point2), list(point3)]
    return triangle

def generator_of_lines(list_points: list, itinerary: list) -> list:
    """Function generator lines from points"""
    
    lines: list = []
    for i in range(len(itinerary) - 1):#TODO! -> list comp-s
        lines.append([list_points[itinerary[i]], list_points[itinerary[i + 1]]])
    return (lines)

def plot_trinagle_generated_simple(triangle: list, thename: str) -> None:
    """draw elementary picture of simple trinagle"""
    
    figure, ax_coords = pl.subplots()
    xs_base = [triangle[0][0], triangle[1][0], triangle[2][0]]
    ys_base = [triangle[0][1], triangle[1][1], triangle[2][1]]
    
    itin = [0, 1, 2, 0]

    
    lc_base = mc.LineCollection(generator_of_lines(triangle, itin), linewidths=3)
    ax_coords.add_collection(lc_base)
    ax_coords.margins(0.2)
    pl.scatter(xs_base, ys_base)
    pl.show()
    #pl.savefig(str(thename) + '.png')#TODO -> used tempfile
    #pl.close()
    
    
plot_trinagle_generated_simple(from_points_to_triangle((0.2, 0.8), (0.5, 0.2), (0.8, 0.7)), 'Triangle')


def get_distance(point1: list, point2: list) -> float:
    """Return distance between points with Pifagore theorem"""
    
    distance: float = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

