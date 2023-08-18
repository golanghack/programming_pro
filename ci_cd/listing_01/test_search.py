#! /usr/bin/env python3 

from search import search

def test_search():
    """Testing search function"""

    assert search(3, [1, 2, 3, 4]) == 2, 'target in stack'

def test_search_first_element_as_a_target():
    """Testing search first element in list""" 

    assert search(1, [1, 2, 3, 4]) == 0, 'first element'

def test_search_last_element_as_a_target():
    assert search(4, [1, 2, 3, 4]) == 3, 'last element'