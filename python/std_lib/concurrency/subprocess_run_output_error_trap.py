#! /usr/bin/env python3 

import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>%2; exit1', 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
    )

except subprocess.CalledProcessError as err:
    print(f'ERROR -> {err}')

else:
    print('return -> ', completed.returncode)
    print(f'Have {len(completed.stdout)} bytes in stdout {completed.stdout.decode("utf-8")!r}')
    print(f'Have {len(completed.stderr)} bytes in stderr -> {completed.stderr.decode("utf-8")!r}')
    