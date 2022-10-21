#! /usr/bin/env python3

"""Russian Peasant Multiplication."""
from math import floor as fl
import pandas as pd

def user_numbers(msg):
    try:
        line_one_number = input(msg)
        line_two_number = input(msg)
        
        one_number = int(line_one_number)
        two_number = int(line_two_number)
    except ValueError as err:
        print(err)
    return one_number, two_number

start_number, end_number = user_numbers('Enter numbers--> ')  

graf_divide = [start_number]
graf_multiply = [end_number]

while min(graf_divide) > 1:
    graf_divide.append(fl(min(graf_divide) / 2))
        
while (len(graf_multiply) < len(graf_divide)):
    graf_multiply.append(max(graf_multiply) * 2)
    
    
graf_halfy = pd.DataFrame(zip(graf_divide, graf_multiply))
graf_halfy = graf_halfy.loc[graf_halfy[0] % 2 == 1, :]
full_summ = sum(graf_halfy.loc[:, 1])
    
print(full_summ)