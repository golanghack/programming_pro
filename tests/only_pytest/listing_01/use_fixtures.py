#! /usr/bin/env python3 

import pytest 

@pytest.mark.usefixtures('provide_current_time')
class TestMulti:
    
    def test_first(self):
        print('Running at -> ', self.now)
        assert 5 == 5 
        
    @pytest.mark.usefixtures('greet')
    def test_second(self):
        assert 10 == 10 
        
@pytest.fixture
def greet():
    print('Hello')
    yield 
    print('Bue')
    
@pytest.fixture(scope='class')
def provide_current_time(request):
    import datetime
    request.cls.now = datetime.datetime.utcnow()
    print('enter cls -->')
    yield 
    print('exit cls  -->')