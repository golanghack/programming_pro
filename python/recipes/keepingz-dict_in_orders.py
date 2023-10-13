#! /usr/bin/env python3 

""" 
Problem 

You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.
""" 

from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3

for key in od:
    print(key, od[key])

""" 
>>> import json
>>> json.dumps(od)
'{"one": 1, "two": 2, "three": 3}'
""" 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
