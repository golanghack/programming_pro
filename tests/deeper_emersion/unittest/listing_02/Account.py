#! /usr/bin/env python3 

class Account(object):
    """Simple class for testing."""
    
    def __init__(self, data_interface: str) -> None:
        self.data_int = data_interface
        
    def get_account(self, id_num: int) -> int:
        return self.data_int.get(id_num)
    
    