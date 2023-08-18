#! /usr/bin/env python3 

import tempfile
import pytest 
from myapp import setup

@pytest.fixture
def setup_app():
    setup()
    tempfile.gettempdir()
    