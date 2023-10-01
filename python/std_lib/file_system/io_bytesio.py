#! /usr/bin/env python3 

import io 

# writing
output = io.BytesIO()
output.write('This goes into the buffer .'.encode('utf-8'))
output.write('Français'.encode('utf-8'))

# read 
print(output.getvalue())
output.close()

# initialization buffer
input_ = io.BytesIO(b'Initial value for read buffer')

# read from buffer
print(input_.read())