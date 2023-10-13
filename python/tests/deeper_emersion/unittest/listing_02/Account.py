#! /usr/bin/env python3 

import requests
from typing import Any
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
    
    def get_current_balance(self, id_num: int) -> Any:
        """Get balance."""
        
        response = requests.get('https://some-account-uri/' + id_num)
        return {'status': response.status_code, 
                'data': response.text}
    
    def add_account(self, account: str):
        self.accounts[account.account_number] = account.balance