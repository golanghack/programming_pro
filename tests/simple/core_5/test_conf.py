#! /usr/bin/env python3 

import os 
import tempfile
from unittest import mock 
import pytest

class DataBaseFixture:
    
    def __init__(self) -> None:
        self.db_file = self.create_temporary_db()
        self.session = self.connect_db(self.db_file)
        
    def tear_down(self):
        self.session.close()
        os.remove(self.db_file)
        
    def create_temporary_db(self) -> str:
        return tempfile.NamedTemporaryFile(delete=False).name
    
    def connect_db(self, db_file: str) -> mock.MagicMock:
        return mock.MagicMock()
    
    def create_table(self, table_name: str, **fields: str):
        pass
    
    def check_row(self, table_name: str, **quesry: str):
        pass
    
@pytest.fixture
def db_testing():
    fixture = DataBaseFixture()
    yield fixture
    fixture.tear_down()
