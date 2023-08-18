#! /usr/bin/env python3 

import pickle
import sys 

class SimpleObject:
    
    def __init__(self, name: str) -> None:
        self.name = name
        list_name = list(name)
        list_name.reverse()
        self.name_backwards = ''.join(list_name)
        
if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('preserve'))
    data.append(SimpleObject('last'))
    
    filename = sys.argv[1]
    
    with open(filename, 'wb') as out:
        for obj in data:
            print(f'WRITING -> {obj.name} ({obj.name_backwards})')
            pickle.dump(obj, out)