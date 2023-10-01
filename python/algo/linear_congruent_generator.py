#! /udr/bin/env python3 

"""<--ALGO LINEAR CONGRUENT GENERATOR-->"""

import matplotlib.pyplot as plt 


def linear_congruent_gen(paste: int, number_one: int, number_two: int, number_three: int) -> int:
    """linear gongruent generator is function for generate pseudo sporadic numbers"""
    
    next_ = (paste * number_one + number_two) % number_three
    return next_

def massive_pseudo_numbers(n1: int, n2: int, n3: int) -> list:
    out = [1]
    while len(out) <= n3:
        out.append(linear_congruent_gen(out[len(out) - 1], n1, n2, n3))
        
    return out



def over_summ(lst: list, sum_lenght: int) -> list:
    """DIEHARD TEST"""
    
    lenght_lst = len(lst)
    lst.extend(lst)
    out = []
    for i in range(0, lenght_lst):
        out.append(sum(lst[i:(i + sum_lenght)]))
    return out

"""ILLUSTRATED"""

over = over_summ(massive_pseudo_numbers(211111, 111112, 300007), 12)
plt.hist(over, 20, facecolor='red', alpha=0.5)
plt.title('result of one diehard test -> over sums')
plt.xlabel('Sum of Elements of Over Consecutive Sections of List')
plt.ylabel('Frequency of sum')
plt.show()