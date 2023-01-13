#! /usr/bin/env python3 

import pytest
from cards import Card

@pytest.fixture(params=['done', 'in prog', 'todo'])
def start_state(request):
    return request.param