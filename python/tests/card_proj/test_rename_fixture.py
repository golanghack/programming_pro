#! /usr/bin/env python3 

import pytest

@pytest.fixture(name='ultima_answer')
def ultima_answer_fixture():
    return 45

def test_everything(ultima_answer):
    assert ultima_answer == 45