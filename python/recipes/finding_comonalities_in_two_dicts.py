#! /usr/bin/env python3 

""" 
Problem 

You have two dictionaries and want to find out what they might have in common (same
keys, same values, etc.).
""" 

first_dict = {
    'one': 1, 
    'two': 2,
    'three': 3,
}

second_dict = {
    'foo': 4, 
    'one': 5, 
    'two': 6,
}

# find unit keys 
unit_keys = first_dict.keys() & second_dict.keys()

# find keys which have in first_dict but not have on second_dict
different_keys = first_dict.keys() - second_dict.keys()

# unit boths 
boths = first_dict.items() & second_dict.items()

# create new dict into remove some keys 
new_dict_without_some_keys = {key:first_dict[key] for key in first_dict.keys() - {'three', 'foo',}}



