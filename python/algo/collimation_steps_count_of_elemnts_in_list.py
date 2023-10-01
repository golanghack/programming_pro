#! /usr/bin/env python3

import math 
import numpy as np 
import random
import matplotlib.pyplot as plt

def insert_list(lst, to_insert):
    """insert_list sorting with insert"""
    
    check_location_number = len(lst) - 1
    insert_number = 0
    global stepcounter
    stepcounter = 0
    #main algo while 
    while(check_location_number >= 0):
        stepcounter += 1
        if to_insert > lst[check_location_number]:
            insert_number = check_location_number + 1
            check_location_number = -1
        if to_insert == 0:
            lst[0] = to_insert
            del(lst[0])
            break
        check_location_number -= 1
    stepcounter += 1
    lst.insert(insert_number, to_insert)
    return lst 

def insertion_list(old_lst):
    """insert_list sorting with insert"""
    new_lst = []
    global stepcounter
    stepcounter = 0
    while len(old_lst) > 0:
        stepcounter += 1
        to_insert = old_lst.pop(0)
        new_lst = insert_list(new_lst, to_insert)
    return new_lst

def check_steps(size_of_lst):
    lst = [int(10000 * random.random()) for i in range(size_of_lst)]
    global stepcounter 
    stepcounter = 0
    insertion_list(lst)
    return stepcounter

if __name__ == '__main__':
    random.seed(5040)
    xs = list(range(1, 100))
    ys = [check_steps(x) for x in xs]
    ys_exponent = [math.exp(x) for x in xs]
    xs_squared = [x**2 for x in xs]
    xs_threehalves = [x**1.5 for x in xs]
    xs_cubed = [x**3 for x in xs]
    plt.plot(xs, ys)
    plt.plot(xs, xs_squared)
    plt.plot(xs, xs_cubed)
    plt.plot(xs, xs_threehalves)
    axes = plt.gca()
    axes.set_ylim([np.min(ys), np.max(ys) + 140])
    plt.plot(xs, ys_exponent)
    plt.title('Insertion Sort to Exponent')
    plt.xlabel('Number --> ')
    plt.ylabel('Steps --> ')
    plt.show()