#! /usr/bin/env python3 

import pytest
from somewhere import app

@pytest.fixture(scope='session', name='app') 
def _app():
    """The app object."""
    yield app()
    
def test_that_uses_app(app):
    assert app.some_property == 'something'