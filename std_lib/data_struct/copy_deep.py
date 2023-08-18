#! /usr/bin/env python3 

import copy
import functools

@functools.total_ordering
class MyClass:
    
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other) -> bool:
        return self.name == other.name 
    
    def __gt__(self, other) -> bool:
        return self.name > other.name
    
a = MyClass('a')
my_list = [a]
dublicate = copy.deepcopy(my_list)

print('---------- my_list --> ', my_list)
print('---------- dublicate > ', dublicate)
print('---------- dublicate is my_list -> ', (dublicate is my_list))
print('---------- dublicate == my_list -> ', (dublicate == my_list))
print('dublicate[0] is my_list[0] -> ', (dublicate[0] is my_list[0]))
print('dublicate[0] == my_list[0] -> ', (dublicate[0] == my_list[0]))