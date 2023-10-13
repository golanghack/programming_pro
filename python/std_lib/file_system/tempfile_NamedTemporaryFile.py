#! /usr/bin/env python3 

import os 
import pathlib
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print('temp -> ')
    print(f'  {temp!r}')
    print('temp.name -> ')
    print(f'  {temp.name!r}')
    f = pathlib.Path(temp.name)
    
print('Exists after close -> ', f.exists())