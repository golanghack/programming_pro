#! /usr/bin/env python3 

import json
import json_myobj

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        print('default(', repr(obj), ')')
        # mutation from obj to dict
        dict_from_obj = {
            '__class__': obj.__class__.__name__,
            '__module__': obj.__module__,
        }

        dict_from_obj.update(obj.__dict__)
        return dict_from_obj

obj = json_myobj.MyClass('internal data')
print(obj)
print(MyEncoder().encode(obj))
