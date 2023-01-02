#! /usr/bin/env python3 

import string

class MyTemplate(string.Template):
    """My template build and used"""
    
    delimeter:str = '%'
    idpattern:str = '[a-z]+ _[a-z]+'
    
template_text = """ 
                    Delimeter : %%
                    Replaced : %with_underscore
                    Ignored : %notunderscored
                """
d = {
        'with_underscore': 'replaced',
        'notunderscored': 'not replaced',
    }
    
t = MyTemplate(template_text)

print('Modified ID pattern -->')
print(t.safe_substitute(d))
