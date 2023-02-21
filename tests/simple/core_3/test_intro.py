#! /usr/bin/env python3 

import csv
from typing import List, Tuple
from series import highest_rated, oldest
import pytest


@pytest.fixture
def comedy_series():
    return [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]

def test_highet_rated__() -> None:
    series = [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]
    
    assert highest_rated(series) == 'Seinfeld'
    
def test_oldest__() -> None:
    series = [
        ("The Office", 2005, 8.8),
        ("Scrubs", 2001, 8.4),
        ("IT Crowd", 2006, 8.5),
        ("Parks and Recreation", 2009, 8.6),
        ("Seinfeld", 1989, 8.9),
    ]
    
    assert oldest(series) == 'Seinfeld'
    
def test_highest_rated(comedy_series) -> None:
    assert highest_rated(comedy_series) == 'Seinfeld'
    
def test_oldest(comedy_series) -> None:
    assert oldest(comedy_series) == 'Seinfeld'
    
class Test:
    
    @pytest.fixture
    def drama_series(self) -> List[Tuple[str, int, int]]:
        return [
            ("The Mentalist", 2008, 8.1),
            ("Game of Thrones", 2011, 9.5),
            ("The Newsroom", 2012, 8.6),
            ("Cosmos", 1980, 9.3),
        ]
        
    def test_highest_rated(self, drama_series) -> None:
        assert highest_rated(drama_series) == 'Game of Thrones'
        
    def test_oldest(self, drama_series) -> None:
        assert oldest(drama_series) == 'Cosmos'