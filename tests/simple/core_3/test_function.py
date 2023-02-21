#! /usr/bin/env python3 

from unittest.mock import MagicMock
import pytest

class WindowManager:
    """Managing abstract window class."""
    
    def __init__(self, log) -> None:
        self.log = log
        
    def close(self):
        pass
    
    def new_help_window(self, fn) -> MagicMock:
        window = MagicMock()
        window.title.return_value = 'Pipe Setup Help'
        return window
    
@pytest.fixture
def manager() -> WindowManager:
    return WindowManager('log')

def create_window_manager():
    return WindowManager('log')

def test_window_creator() -> None:
    manager = create_window_manager()
    window = manager.new_help_window('pipes_help.rst')
    assert window.title() == 'Pipe Setup Help'
    
