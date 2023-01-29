#! /usr/bin/env python3 

import array
import binascii
import tempfile

a = array.array('i', range(5))
print('ALL -> ', a)

#write massive of numbers in tempfile
output = tempfile.NamedTemporaryFile()
a.tofile(output.file) # real file
output.flush()

# reading row bytes date
with open(output.name, 'rb') as input_:
    raw_data = input_.read()
    print('Row contents -> ', binascii.hexlify(raw_data))
    
    #reading date in massive
    input_.seek(0)
    a2 = array.array('i')
    a2.fromfile(input_, len(a))
    print('A2 -> ', a2)
    