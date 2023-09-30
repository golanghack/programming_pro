#! /usr/bin/env python3 

"""Create function mutation from vector to unit vector"""
import numpy as np 

def create_unit(vector):
    """Return unit vector from this vector"""

    lenght = []
    for i in vector:
        lenght.append(i ** 2)

    unit_vector = vector / (sum(lenght) ** .5)
    return unit_vector

my_vector = np.array([1, 2, 3])
print(create_unit(my_vector))