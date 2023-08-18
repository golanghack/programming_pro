#! /usr/bin/env python3 

import csv
from collections import namedtuple

DATA_SET = """ 
Main Grid, 48, 44
2nd Grid, 24, 21
3rd Grid, 24, 0
"""

GridData = namedtuple('GridData', 'name total_cells active_cells')

def convert_size(s: str) -> int:
    """Converter sizing from str(or list) to int."""
    
    return int(float(s))

def parse_grid_data(fields: list) -> tuple:
    """Parser for GridData on fields."""
    
    return GridData(
        name=str(fields[0]), 
        total_cells=convert_size(fields[1]), 
        active_cells=convert_size(fields[2]),
    )
    
def iter_grids_from_csv(lines: str) -> None:
    """Iterator for csv file."""
    
    for fields in csv.reader(lines):
        yield parse_grid_data(fields)
        
def test_read_properties() -> None:
    lines = DATA_SET.strip().splitlines()
    grids = list(iter_grids_from_csv(lines))
    
    assert grids[0] == GridData('Main Grid', 48, 44)
    assert grids[1] == GridData('2nd Grid', 24, 21)
    assert grids[2] == GridData('3rd Grid', 24, 0)