#! /usr/bin/env python3 

import io 
import pickle
from pprint import pprint

class SimpleObject:
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.name_backwards = name[::-1]
        return
    
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# file imitation
out_s = io.BytesIO()

# write ti stream
for obj in data:
    print(f'WRITING -> {obj.name} ({obj.name_backwards})')
    pickle.dump(obj, out_s)
    out_s.flush()
    
# settings reading stream
in_s = io.BytesIO(out_s.getvalue())

# read data 
while True:
    try:
        obj = pickle.load(in_s)
    except EOFError:
        break
    else:
        print(f'READ -> {obj.name} ({obj.name_backwards})')
        
        