#! /usr/bin/env python3 

def test_tmp_path(tmp_path):
    """function scope"""
    file = tmp_path / 'file.txt'
    file.write_text('Hello')
    assert file.read_text() == 'Hello'
    
def test_tmp_path_factory(tmp_path_factory):
    """Session scope."""
    path = tmp_path_factory.mktemp('sub')
    file = path/'file.txt'
    file.write_text('Hello')
    assert file.read_text() == 'Hello'
    
    