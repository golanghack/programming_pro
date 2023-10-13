#! /usr/bin/env python3 
"""Find norm of vector"""
import numpy as np 

my_vector = np.array([1, 2, 3])
my_vector_square = []
for i in my_vector:
    my_vector_square.append(i ** 2)

my_norm = sum(my_vector_square) ** .5
np_norm = np.linalg.norm(my_vector)
print(f'my norm -> {my_norm}')
print(f'np norm -> {np_norm}')
