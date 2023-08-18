#! /usr/bin/env python3

from subprocess import run 

def test_hello() -> bool:
    result = run(['python3', 'hello.py'], capture_output=True, text=True)
    output = result.stdout
    assert output == 'Hello\n'