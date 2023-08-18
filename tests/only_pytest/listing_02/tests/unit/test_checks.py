#! /usr/bin/env python3 

import pytest
from src.fizzbuzz import is_fizz, is_buzz

@pytest.mark.parametrize('n, res', [
    (1, False), 
    (3, True), 
    (4, False), 
    (6, True),
])

def test_is_fizz(n, res):
    assert is_fizz(n) is res 

@pytest.fixture(scope='function')
def divisible_by_5(n):
    return n % 5 == 0 

@pytest.mark.parametrize('n', [
    1, 3, 5, 6, 10,
])

def test_is_buzz(n, divisible_by_5):
    assert is_buzz(n) is divisible_by_5