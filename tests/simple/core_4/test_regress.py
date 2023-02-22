#! /usr/bin/env python3 

from data_
from typing import List, Dict
def obtain_series() -> List[Dict]:
    return [
        dict(name='The Office', year=2005, rating=8.8), 
        dict(name='Scrubs', year=2001, rating=8.4), 
        dict(name='IT Crowd', year=2006, rating=8.5),
        dict(name='Parks and Recreation', year=2009, rating=8.6),
        dict(name='Seinfeld', year=1989, rating=8.9), 
        dict(name='Rock and Morty', year=2013, rating=9.3),
    ]
    
def test_obtain_series_asserts() -> None:
    data = obtain_series()
    
    assert data[0]['name'] == 'The Office'
    assert data[0]['year'] == 2005
    assert data[0]['rating'] == 8.8
    assert data[1]['name'] == 'Scrubs'
    assert data[1]['year'] == 2001
    assert data[1]['rating'] == 8.4
    
    
def test_obtain_series(data_regressions):
    data = obtain_series()
    data_regression.check(data)