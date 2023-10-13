#! /usr/bin/env python3

import pytest

@pytest.mark.timeout(10)
class TestCore:
    
    def test_simple_simulation(self):
        pass
    def test_compute_tracers(self):
        pass

class TestTwo(TestCore):
    
    def test_pipes(self):
        pass
     

