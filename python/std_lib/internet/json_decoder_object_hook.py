#! /usr/bin/env python3 

import json

class MyDecoder(json.JSONDecoder):

    def __init__(self):
        json.JSONDecoder.__init__(
            self, 
            object_hook=self.from_dict_to_object,
        )

    def from_dict_to_object(self, obj_dict):
        if '__class__' in obj_dict:
            class_name = obj_dict.pop('__class__')
            module_name = obj_dict.pop('__module__')
            module = __import__(module_name)

            print('MODULE -> ', module.__name__)
            class_ = getattr(module, class_name)
            print('CLASS -> ', class_)

            args = {
                key: value 
                for key, value in obj_dict.items()
            }

            print('INSTANCE ARGS -> ', args)
            inst = class_(**args)
        else:
            inst = obj_dict
        return inst

encoded_object = ''' 
[{"s": "instance value goes here", 
    "__module__": "json_myobj", 
    "__class__": "MyClass"}]
''' 

myobj_instance = MyDecoder().decode(encoded_object)
print(myobj_instance)