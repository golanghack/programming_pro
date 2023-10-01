#! /usr/bin/env python3 

import pytest

@pytest.mark.first
def test_one():
    assert True
    
def test_two():
    assert True