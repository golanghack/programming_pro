#! /usr/bin/env python3 

import io 
import json

data = [
    {
        'a': 'A', 
        'b': (2, 4), 
        'c': 5.9,
    },
]

file_input = io.StringIO()
json.dump(data, file_input)

print(file_input.getvalue())