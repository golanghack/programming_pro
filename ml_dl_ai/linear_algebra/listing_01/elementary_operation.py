#! /usr/bin/env python3 

"""ELEMENTARY OPERATIONS WITH VECTOR`S"""

import numpy as np 

# summ
vector_one = np.array([4, 5, 6])
vector_two = np.array([10, 40, 50])
vector_three = np.array([0, 3, 5, 9])

one_with_two = vector_one + vector_two # OK
#one_with_three = vector_one + vector_three # ERROR

# translation
# dont correct summary another vectors 
# with differents shape
vector_column = np.array([[66, 77, 88]])
vector_row = np.array([[10, 20, 30]]).T # <--


# dont ecvivalnt list <==> np.array 
number = 2
massive_a = [2, 4, 6]
massive_b = np.array(massive_a)
"""
>>> print(massive_a * number) # [2, 4, 6, 2, 4, 6]
>>> print(massive_b * 2) # [4 8 12]
if number = float(number) ->
>>> print(massive_b) # [2, 4, 6]
>>> print(massive_a * number) # ERROR
""" 

# summ number and vector
number = 2
vector = np.array([6, 12])
sum_n_and_v = number + vector # [8 14]

# trans
vector_col = np.array([[1, 2, 3]]).T
vector_row = np.array([[10, 20]])
vector_col + vector_row

""" 
>>> array([[11, 21],[12, 22],[13, 23]])
"""
# alternative 
vector_row = np.array([[1, 2, 3]])
vector_col = np.array([[10, 20]]).T 
vector_col + vector_row
""" 
>>> array([[11, 12, 12], [21, 22, 23]])
""" 

# mathematical lenght/geometrical lenght/python len
vector = np.array([1, 2, 3, 4, 5])
math_len = len(vector) # 5
module_len = np.linalg.norm(vector) # norm of vector

# dotted
number = 10
vector = np.array([1, 2, 3, 4, 5])
vector_second = np.array([5, 6, 7, 8, 9])
"""
print(np.dot(vector, vector_second)) # 115
print(np.dot(number * vector, vector_second)) # 1150
"""

# adamar 
vector_a = np.array([50, 50, 50])
vector_b = np.array([1, 2])

""" 
>>> print(vector_a * vector_b) # ERROR
change lenght vectors <==> equal
>>> vector b = np.array([1, 2, 1])
>>> print(vector_a * vector_b) # OK
""" 

# gram-shmidt
vector_one = np.array([1, 2, 3])
vector_two = np.array([9, 8, 7])

"""
beta = (vector_one.T * vector_two) / (vector_one.T * vector_one)
print(beta) # [9.         4.         2.33333333]
# test 
print((vector_one.T * vector_two) - (beta * vector_one.T * vector_one) == 0) # True
""" 


