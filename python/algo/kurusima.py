#! /usr/bin/env  python3 

"""<--KURUSIMA ALGO FOR MAGIC SQUARE-->"""

import math
import random

#size matrix(square)tax
n = 11

square = [[float('nan') for i in range(0, n)] for j in range(0, n)]

#coordinates of center square
center_i = math.floor(n / 2) 
center_j = math.floor(n / 2)


#kurusima table
""" 
table -> centers of square`s Kurusima
|n 2|  |n|  |(n 2 + 1) / 2|
|n|    |2 + 1 – n|    1
"""
square[center_i][center_j] = int((n ** 2 + 1) / 2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n ** 2
square[center_i][center_j + 1] = n ** 2 + 1 - n 
square[center_i][center_j - 1] = n 

def best_print_square(square):
    """This function bieutifully print square."""
    labels = ['[' + str(x) + ']' for x in range(0, len(square))]
    format_row = '{:>6}' * (len(labels) + 1)
    print(format_row.format('', *labels))
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))
        
#functions for three rules Kurusima

def first_rule(x, n, up_tear_down=False):
    return ((x + ((-1) ** up_tear_down) * n) % n ** 2)


def second_rule(x, n, right_or_left=True):
    return ((x + ((-1) ** right_or_left)) % n ** 2)


def three_rule(x, n, right_or_left=True):
    return ((x + ((-1) ** right_or_left * (-n + 1))) % n ** 2)


#sporadic choice walking matrix
entry_i = center_i
entry_j = center_j

#direction -> all 4directions
where_we_can_go = []

if (entry_i < (n - 1) and entry_j < (n - 1)):
    where_we_can_go.append('down_right')

if(entry_i < (n - 1) and entry_j > 0):
    where_we_can_go.append('down_left')
    
if(entry_i > 0 and entry_j < (n - 1)):
    where_we_can_go.append('up_right')
    
    
if(entry_i > 0 and entry_j > 0):
    where_we_can_go.append('up_left')

#sporadic choice
where_to_go = random.choice(where_we_can_go)

# choice rules 
if (where_to_go == 'up_right'):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = first_rule(square[entry_i][entry_j], n, True)
    
if(where_to_go == 'down_left'):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = first_rule(square[entry_i][entry_j],n,False)
    
if(where_to_go == 'up_left'):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = second_rule(square[entry_i][entry_j],n,True)
    
    
if(where_to_go == 'down_right'):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = second_rule(square[entry_i][entry_j],n,False)
    
if(where_to_go == 'up_left' and (entry_i + entry_j) == (n)):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = three_rule(square[entry_i][entry_j],n,True)
    
    
if(where_to_go == 'down_right' and (entry_i + entry_j) == (n-2)):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = three_rule(square[entry_i][entry_j],n,False)

def fillsquare(square, entry_i, entry_j, howfill):
    while(sum(math.isnan(i) for row in square for i in row) > howfill):
        where_we_can_go = []
        
        if(entry_i < (n - 1) and entry_j < (n - 1)):
            where_we_can_go.append('down_right')
            
        if(entry_i < (n - 1) and entry_j > 0):
            where_we_can_go.append('down_left')
            
        if(entry_i > 0 and entry_j < (n - 1)):
            where_we_can_go.append('up_right')
            
        if(entry_i > 0 and entry_j > 0):
            where_we_can_go.append('up_left')
            
        where_to_go = random.choice(where_we_can_go)
        
        if(where_to_go == 'up_right'):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = first_rule(square[entry_i][entry_j],n,True)
            
        if(where_to_go == 'down_left'):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = first_rule(square[entry_i][entry_j],n,False)
            
        if(where_to_go == 'up_left' and (entry_i + entry_j) != (n)):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = second_rule(square[entry_i][entry_j],n,True)
            
        if(where_to_go == 'down_right' and (entry_i + entry_j) != (n-2)):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = second_rule(square[entry_i][entry_j],n,False)
            
        if(where_to_go == 'up_left' and (entry_i + entry_j) == (n)):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = three_rule(square[entry_i][entry_j],n,True)
            
        if(where_to_go == 'down_right' and (entry_i + entry_j) == (n-2)):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = three_rule(square[entry_i][entry_j],n,False)
        entry_i = new_entry_i
        entry_j = new_entry_j
    return square

square = fillsquare(square, entry_i, entry_j, (n ** 2) / 2 - 4)

square = [[n ** 2 if x == 0 else x for x in row] for row in square]

entry_i = math.floor(n / 2) + 1
entry_j = math.floor(n / 2)

square = fillsquare(square, entry_i, entry_j, 0)

square = [[n ** 2 if x == 0 else x for x in row] for row in square]

print(square)