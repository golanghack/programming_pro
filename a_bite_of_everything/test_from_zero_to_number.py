#! /usr/bin/env python3 

from from_zero_to_number import from_zero_to_number

def test_from_zero_to_number() -> None:
    assert from_zero_to_number(10) == [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900]