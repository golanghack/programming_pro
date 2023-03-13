#! /usr/bin/env python3

import pytest

pytest_plugins = ['src.fizzbuzz.testing.fixtures']

def pytest_runtest_setup(item):
    print('Hooking announce', item)

@pytest.fixture(scope='function', autouse=True)
def enter_exit():
    print('ENTER')
    yield 
    print('EXIT')

def pytest_addoption(parser):
    parser.addoption(
        '--upper', 
        action='store_true',
        help='test for uppercase behavior',
    )