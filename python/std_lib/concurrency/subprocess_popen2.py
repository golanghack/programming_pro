#! /usr/bin/env python3 

import subprocess

print('popen2 -> ')

proc = subprocess.Popen(
    ['cat', '-'], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE,
)

message = 'through stdin to stdout'.encode('utf-8')
stdout_value = proc.communicate(message)[0].decode('utf-8')
print('pass throught -> ', repr(stdout_value))