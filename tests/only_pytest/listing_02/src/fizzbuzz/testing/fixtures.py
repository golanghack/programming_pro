#! /usr/bin/env python3 

import pytest

@pytest.fixture(scope='function', autouse=True)
def announce(request):
    print('RUNNING', request.function)