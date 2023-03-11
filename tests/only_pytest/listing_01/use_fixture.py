#! /usr/bin/env python3 

import pytest

@pytest.fixture
def greet():
    print('Hello')
    yield 
    print('Godbue')
    
class TestMulti:
    
    def test_first(self):
        assert 5 == 5
        
    @pytest.mark.usefixtures('greet')
    def test_second(self):
        assert 10 == 10
        
        