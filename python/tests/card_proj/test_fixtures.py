#! /usr/bin/env python3 

import pytest

@pytest.fixture()
def some_data():
    """Return answer to ultim question."""
    return 45

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 45
    
