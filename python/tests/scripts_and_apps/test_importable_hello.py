#! /usr/bin/env python3 

import script_importable_hello

def test_main(capsys) -> bool:
    script_importable_hello.main()
    output = capsys.readouterr().out
    assert output == 'Hello\n'