#! /usr/bin/env python3 

import json
import json_myobj

my_obj = json_myobj.MyClass('instance value goes here')

print('First attempt')
try:
    print(json.dumps(my_obj))
except TypeError as err:
    print(f'ERROR -> {err}')

def convert_to_builtin_type(obj: object) -> dict:
    """Converting custom data type in standart type"""

    print('default (', repr(obj), ')')
    # from obj to dict
    from_obj_to_dict = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    from_obj_to_dict.update(obj.__dict__)
    return from_obj_to_dict

print()
print('With default')
print(json.dumps(my_obj, default=convert_to_builtin_type))