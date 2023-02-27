#! /usr/bin/env python3 

import io 

# writing 
output = io.StringIO()
output.write('This goes into the buffer. ')
print('And so does this.', file=output)

# read 
print(output.getvalue())
output.close()

# read buffer initialization
input_ = io.StringIO('Initial value for read buffer.')

# read from buffer
print(input_.read())