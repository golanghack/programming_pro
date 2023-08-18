#! /usr/bin/env python3 

import csv
import shutil
import tempfile
import unittest
from collections import namedtuple
from pathlib import Path
from typing import Any, List, Tuple

DATA = """ 
Main Grid,48,44
2nd Grid,24,21
3rd Grid,24,48
"""

GridData = namedtuple('CridData', 'name total_cells active_cells')

def convert_size(sizing: Any) -> int:
    return int(sizing)

def parse_grid_data(fields: List) -> Tuple:
    return GridData(
        name=str(fields[0]), 
        total_cells=convert_size(fields[1]), 
        active_cells=convert_size(fields[2]),
    )
    
def iter_grid_from_csv(path: str) -> None:
    with path.open() as file_:
        for fields in csv.reader(file_.readlines()):
            yield parse_grid_data(fields)
            
class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = Path(tempfile.mktemp())
        cls.filepath = cls.temp_dir / 'data.csv'
        cls.filepath.write_text(DATA.strip())
        
    @classmethod
    def tearDownCase(cls):
        shutil.rmtree(cls.temp_dir)
        
    def setUp(self):
        self.grids = list(iter_grid_from_csv(self.filepath))
        
    def test_read_properties(self):
        self.assertEqual(self.grids[0], GridData('Main Grid', 48, 44))
        self.assertEqual(self.grids[1], GridData('2nd Grid', 24, 21))
        self.assertEqual(self.grids[2], GridData('3rd Grid', 24, 48))
        
    def test_invalid_path(self):
        with self.assertRaises(IOError):
            list(iter_grid_from_csv(Path('invalid file')))
            
    @unittest.expectedFailure
    def test_write_properties(self):
        self.fail('not implemented yet')