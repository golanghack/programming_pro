#! /usr/bin/env python3 

import io 
import os 
import shutil
import sys 

class VerboseStringIO(io.StringIO):
    
    def read(self, n: int=-1):
        next_ = io.StringIO.read(self, n)
        print(f'read({n}) got {len(next_)} bytes.')
        return next_
    
sporadic = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Delectus impedit provident commodi 
optio corporis nisi non eum magnam, ducimus quaerat
expedita illum inventore dolor veritatis reprehenderit ve
l itaque facilis. Eaque.
'''
print('DEFAULT -> ')
input_ = VerboseStringIO(sporadic)
output = io.StringIO()
shutil.copyfileobj(input_, output)
print()

print('ALL ON ONCE -> ')
input_ = VerboseStringIO(sporadic)
output = io.StringIO()
shutil.copyfileobj(input_, output, -1)
print()

print('BLOCKS OF 256 -> ')
input_ = VerboseStringIO(sporadic)
output = io.StringIO()
shutil.copyfileobj(input_, output, 256)