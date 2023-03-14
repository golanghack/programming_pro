#! /usr/bin/env python3 

import io 
import subprocess

print('One line at a items -> ')
proc = subprocess.Popen(
    'python3 repeater.py', 
    shell=True, 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
)

stdin = io.TextIOWrapper(
    proc.stdin, 
    encoding='utf-8', 
    line_buffering=True, 
)

stdout = io.TextIOWrapper(
    proc.stdout, 
    encoding='utf-8', 
)

for i in range(5):
    line = f'{i}\n'
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())

remainder = proc.communicate()[0].decode('utf-8')
print(remainder)

print()
print('All output at once -> ')
proc = subprocess.Popen(
    'python3 repeater.py', 
    shell=True, 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE,
)

stdin = io.TextIOWrapper(
    proc.stdin, 
    encoding='utf-8',
)

for i in range(5):
    line = f'{i}\n'
    stdin.write(line)

stdin.flush()

output = proc.communicate()[0].decode('utf-8')
print(output)