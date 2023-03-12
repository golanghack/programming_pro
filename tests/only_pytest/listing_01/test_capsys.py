#! /usr/bin/env python3 

import pytest

def my_app():
    
    print('my_app started')

def test_capsys(capsys):
    my_app()

    out, err = capsys.readouterr()

    assert out == 'my_app started\n'