#! /usr/bin/env python3 

"""Common operations on vectors"""

import numpy as np 

# linear-combinations
# TODO NOT USE IN PROD!!!
number_1 = 1
number_2 = 2
number_3 = -3 

vector_1 = np.array([5, 5, 5])
vector_2 = np.array([-4, 0, -4])
vector_3 = np.array([1, 3, 2])

print((number_1 * vector_1) + (number_2 * vector_2) + (number_3 * vector_3)) 


# numpy example
linear = np.zeros(len(vector_1))
list_numbers = [number_1, number_2, number_3]
list_vectors = [vector_1, vector_2, vector_3]
for scalar, vect in zip(list_numbers, list_vectors):
    linear += scalar * vect 

print(linear)

    