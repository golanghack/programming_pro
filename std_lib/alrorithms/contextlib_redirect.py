#! /usr/bin/env python3 

from contextlib import redirect_stdout, redirect_stderr
import io
import sys 

def misbehaving_function(a) -> None:
    sys.stdout.write(f'(stdout) A -> {a!r}\n')
    sys.stderr.write(f'(stderr) A -> {a!r}\n')
    
capture = io.StringIO()
with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)
print(capture.getvalue()) 