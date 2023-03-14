#! /usr/bin/env python3 

import subprocess

print('popen3 -> ')

proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2', 
    shell=True, 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
)

message = 'throught stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(message)

print('pass throught -> ', repr(stdout_value.decode('utf-8')))
print('stderr        -> ', repr(stderr_value.decode('utf-8')))