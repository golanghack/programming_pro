#! /usr/bin/env python3

import pytest

@pytest.mark.slow
def test_long_computation():
    pass

@pytest.mark.timeout(10, method='thred')
def test_topology_sort():
    pass

def test_foo():
    pass
