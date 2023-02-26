#! /usr/bin/env python3 

import string 

def invertcaps(text: str) -> str:
    """ 
    Return new string with invert case.
    """
    
    return ''.join(c.upper() if c in string.ascii_lowercase 
                   else c.lower() 
                   if c in string.ascii_uppercase 
                   else c
                   for c in text)
    
if __name__ == '__main__':
    print(invertcaps('AVFfdfdD'))
    print(invertcaps('ababa'))