#! /usr/bin/env python3 

from operator import * 

list_of_values = [dict(val= -1 * i) for i in range(5)]
print('dictonaries -> ')
print('original -> ', list_of_values)

get_values_list = itemgetter('val')
values = [get_values_list(i) for i in list_of_values]
print('values -> ', values)
print('sorted -> ', sorted(list_of_values, key=get_values_list))

print()
tuple_of_values = [(i, i * -2) for i in range(5)]
print('\nTuples -> ')
print('original -> ', tuple_of_values)
get_values_tuple = itemgetter(tuple_of_values)
values = [get_values_tuple() for i in tuple_of_values]
print('values -> ', values)
print('sorted -> ', sorted(tuple_of_values, key=get_values_tuple))