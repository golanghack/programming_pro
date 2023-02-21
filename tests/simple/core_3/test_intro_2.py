#! /usr/bin/env python3 

import csv
from series import highest_rated, oldest
import pytest

@pytest.fixture 
def comedy_series() -> list:
    with open('series.csv', 'r', newline='') as csv_file:
        return list(csv.reader(csv_file))
    
def test_highest_rated(comedy_series):
    assert highest_rated(comedy_series) == 'Seinfeld'
    
def test_oldest(comedy_series):
    assert oldest(comedy_series) == 'Seinfeld'