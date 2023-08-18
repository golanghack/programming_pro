#! /usr/bin/env python3 

"""<--GEOMETRY-->"""

import math
import pylab as pl 
import numpy as np
from matplotlib import collections as mc 

point: list = [0.8, 0.2]
triangle_simple: list = [[0.8, 0.2], [0.5, 0.2], [0.6, 0.7]]

def triangle_circumcenter(trinagle: list):
    """find trangle circumcenter"""
    
    x = complex(trinagle[0][0], trinagle[0][1])
    y = complex(trinagle[1][0], trinagle[1][1])
    z = complex(trinagle[2][0], trinagle[2][1])
    
    complex_width = z - x 
    complex_width /= y - x 
    
    c = (x - y) * (complex_width - abs(complex_width) ** 2) / 2j /complex_width.imag - x
    radius = abs(c + x)
    return ((0 - c.real, 0 - c.imag), radius)


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

def plot_trinagle_generated_simple(triangles: list, 
                                   centers: list, 
                                   plotcircles, 
                                   plotpoints, 
                                   plottriangles, 
                                   plotvoronov, 
                                   plotvpoints,
                                   thename: str) -> None:
    """draw elementary picture of simple trinagle"""
    
    figure, ax_coords = pl.subplots()
    ax_coords.set_xlim([-0.1, 1.1])
    ax_coords.set_ylim([-0.1, 1.1])
    
    lines = []
    
    for i in range(0, len(triangles)):
        triangle = triangles[i]
        center = centers[i][0]
        radius = centers[i][1]
        itin = [0, 1, 2, 0]
        the_lines = generator_of_lines(triangle, itin)
        xs_base = [triangle[0][0], triangle[1][0], triangle[2][0]]
        ys_base = [triangle[0][1], triangle[1][1], triangle[2][1]]
            
        if plotpoints:
            pl.scatter(xs_base, ys_base)
        ax_coords.margins(0.1)
        
        if plotvpoints:
            pl.scatter(center[0], center[1])
        
        circle = pl.Circle(center, radius, color='b', fill=False)
        
        if plotcircles:
            ax_coords.add_artist(circle)
        if plotvoronov:
            for j in range(0, len(triangles)):
                common = 0
                for k in range(0, len(triangles[i])):
                    for n in range(0, len(triangles[j])):
                        if triangles[i][k] == triangles[j][n]:
                            common += 1
                if common == 2:
                    lines.append([list(centers[i][0]), list(centers[j][0])])
        lc_base = mc.LineCollection(the_lines, linewidths=3)
        ax_coords.add_collection(lc_base)
        if plottriangles:
            
            ax_coords.add_collection(lc_base)
        
    pl.show()
    #pl.savefig(str(thename) + '.png')#TODO -> used tempfile
    #pl.close()

def get_distance(point1: list, point2: list) -> float:
    """Return distance between points with Pifagore theorem"""
    
    distance: float = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

"""
triangle1 = from_points_to_triangle((0.2,0.3),(0.3,0.6),(0.5,0.2))
center1,radius1 = triangle_circumcenter(triangle1)
triangle2 = from_points_to_triangle((0.8,0.1),(0.7,0.5),(0.8,0.9))
center2,radius2 = triangle_circumcenter(triangle2)
plot_trinagle_generated_simple([triangle1,triangle2],[center1,center2],[radius1,radius2],'two')

"""
#delone triangulation algo
def generate_delone(points: list):
    delane = [from_points_to_triangle([-5, -5], [-5, 10], [10, -5])]
    number_point = 0
    
    while number_point < len(points):
        point_add = points[number_point]
        delane_index = 0
        
        invalid = []
        while delane_index < len(delane):
            circumcenter, radius = triangle_circumcenter(delane[delane_index])
            new_distance = get_distance(circumcenter, point_add)
            if (new_distance < radius):
                invalid.append(delane[delane_index])
            delane_index += 1
            
        
        point_invalid = []
        for i in range(0, len(invalid)):
            delane.remove(invalid[i])
            for j in range(0, len(invalid[i])):
                point_invalid.append(invalid[i][j])
        point_invalid = [list(x) for x in set(tuple(x) for x in point_invalid)]
        
        for i in range(0, len(point_invalid)):
            for j in range(i + 1, len(point_invalid)):
                count = 0
                for k in range(0, len(invalid)):
                    count += (1 * (point_invalid[i] in invalid[k]) 
                              * (point_invalid[j] in invalid[k]))
                if (count == 1):
                    delane.append(from_points_to_triangle(point_invalid[i], point_invalid[j], point_add))
        number_point += 1
    return delane


n = 15

np.random.seed(5201314)
xs = np.random.rand(n)
ys = np.random.rand(n)

points = zip(xs, ys)
list_points = list(points)
delane_gen = generate_delone(list_points)

circumcenters = []
for i in range(0, len(delane_gen)):
    circumcenters.append(triangle_circumcenter(delane_gen[i]))
    
plot_trinagle_generated_simple(delane_gen, circumcenters, True, True, True, True, True, 'final')

