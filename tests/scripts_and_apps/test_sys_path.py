#! /usr/bin/env python3 

import sys 

def test_sys_path() -> None:
    print('sys.path -> ')
    for p in sys.path:
        print(p)