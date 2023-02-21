#! /usr/bin/env python3

import csv
import pytest
from typing import List


@pytest.fixture
def series() -> List:
    with open("series.csv", "r", newline="") as file:
        return list(csv.reader(file))
    
GENRE = 4

@pytest.fixture
def comedy_series(series) -> List:
    return [x for x in series if x[GENRE] == "comedy"]