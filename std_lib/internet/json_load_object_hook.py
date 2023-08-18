#! /usr/bin/env python3 

import json 

def dict_to_object(object_dict: dict):
    """Converting dict for custom object from json to custom object."""

    if '__class__' in object_dict:
        class_name = object_dict.pop('__class__')
        module_name = object_dict.pop('__module__')
        module = __import__(module_name)

        print('MODULE -> ', module.__name__)
        class_ = getattr(module, class_name)
        print('CLASS -> ', class_)

        args = {
            key: value
            for key, value in object_dict.items()
        }
        print('INSTANCE ARGS -> ', args)
        inst = class_(**args)

    else:
        inst = object_dict
    return inst

ecnoded_object = ''' 
[{"s": "instance value goes here", 
    "__module__": "json_myobj", 
    "__class__": "MyClass"}]
''' 

myobject_instance = json.loads(
    ecnoded_object, 
    object_hook=dict_to_object,
)

print(myobject_instance)