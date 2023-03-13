#! /usr/bin/env python3 

import subprocess

completed = subprocess.run(
    ['ls', '-l'], 
    stdout=subprocess.PIPE,
)

print('return -> ', completed.returncode)
print(f'Have {len(completed.stdout)} bytes in stdout -> \n{completed.stdout.decode("utf-8")}')
