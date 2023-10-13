#! /usr/bin/env python3 

import io 

# write in buffer 
output = io.BytesIO()
wrapper = io.TextIOWrapper(output, encoding='utf-8', write_through=True,)
wrapper.write('This goes into the buffer.')
wrapper.write('Français')

# read value
print(output.getvalue())
output.close()

# initialization buffer of read
input_ = io.BytesIO(
    b'Initial value for read buffer wirh unicide characters ' +
    'Français'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input_, encoding='utf-8')

#read from buffer 
print(wrapper.read())