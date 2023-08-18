#! /usr/bin/env python3 

import script_function_hello

def test_full_output() -> bool:
    assert script_function_hello.full_output() == 'Hello'
    
def test_main(capsys) -> bool:
    script_function_hello.main()
    output = capsys.readouterr().out
    assert output == 'Hello\n'