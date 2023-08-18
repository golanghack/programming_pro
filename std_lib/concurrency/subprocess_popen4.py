#! /usr/bin/env python3 

import subprocess 

print('popenv4 -> ')
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2', 
    shell=True, 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT,
)

message = 'throught stdin to stdout\n'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(message)
print('combined output -> ', repr(stdout_value.decode()))
print('stderr value -> ', repr(stderr_value))