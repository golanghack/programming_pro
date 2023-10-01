#! /usr/bin/env python3 

import pytest

@pytest.fixture(scope='session', autouse=True)
def setupsuite():
    print('<--Start tests-->')
    yield
    print('<--Finished----->')
    
@pytest.fixture
def random_number_generator():
    import random
    def _number_rpovider():
        return random.choice(range(10))
    yield _number_rpovider
    