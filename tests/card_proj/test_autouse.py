#! /usr/bin/env python3 

import pytest
import time 

@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield 
    now = time.time()
    print('--')
    print(f'finished: {time.strftime("%d%b%X", time.localtime(now))}')
    print('______-----_______')
    
@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start 
    print(f'\n-->TEST--> dyration -> {delta:0.3} seconds')
    
def test_one():
    """Simulate long-ish running test."""
    time.sleep(1)
    
def test_two():
    """Simulate slignly longer test."""
    time.sleep(1.23)
    