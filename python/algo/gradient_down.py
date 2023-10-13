#! /usr/bin/env python3

"""<--GRADIENT DOWN-->"""

threshold = 0.0001
maximum_ierations = 10000

def revenue_derivative(tax):
    return (100 * (1 / (tax + 1) - 2 * (tax - 0.2)))

def revenue_derivative_flipped(tax):
    """Derivative revenue function from program gradient up"""
    
    return (0 - revenue_derivative(tax))

current_rate = 0.7

keep_going = True

step_size = 0.001

iterations = 0

while(keep_going):
    rate_change = step_size * revenue_derivative_flipped(current_rate)
    current_rate = current_rate - rate_change
    if (abs(rate_change) < threshold):
        keep_going = False
    if (iterations >= maximum_ierations):
        keep_going = False
    iterations += 1
    

    