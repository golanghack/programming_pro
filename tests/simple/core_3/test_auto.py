#! /usr/bin/env python3

import json
import os 
import subprocess
import tempfile
from pathlib import Path
import pytest

@pytest.fixture(autouse=True)
def setup_dev_environment() -> None:
    """Set up development environ.
    """
    
    previous = os.environ.get('APP_ENV', '')
    os.environ['APP_ENV'] = 'TESTING'
    yield
    os.environ['APP_ENV'] = previous
    
def test_setup_app():
    pass

@pytest.fixture
def pipenv_dir() -> None:
    import venv
    
    with tempfile.TemporaryDirectory() as directory:
        venv.create(directory)
        pwd = os.getcwd()
        os.chdir(directory)
        yield directory
        os.chdir(pwd)
        
@pytest.mark.usefixture('venv_dir')
class Test:
    
    def test_something(self):
        print([str(x) for x in Path('.').iterdir()])
        assert Path('pyvenv.cfg').is_file() 