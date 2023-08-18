#! /usr/bin/env python3 

import subprocess 

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2', 
        shell=True, 
        stderr=subprocess.STDOUT, 
    )

except subprocess.CalledProcessError as err:
    print(f'ERROR -> {err}')

else:
    print(f'Have {len(output)} bytes in output -< {output.decode("utf-8")!r}')