#! /usr/bin/env python3 

class Account(object):
    """Simple class for testing."""
    
    def __init__(self, data_interface: str) -> None:
        self.data_int = data_interface
        
    def get_account(self, id_num: int) -> int:
        try:
            result = self.data_int.get(id_num)
        except ConnectionError:
            result = 'Connection error occured. Try again.'
        return result
    
    