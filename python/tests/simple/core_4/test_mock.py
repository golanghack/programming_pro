#! /usr/bin/env python3 

import getpass

def user_login(name: str) -> int:
    getpass.getpass('Enter password -> ')
    return 1

def test_login_success(mocker) -> None:
    mocked = mocker.patch.object(getpass, 'getpass', return_value='valid-pass')
    
    assert user_login('test-user')
    mocked.assert_called_with('Enter password -> ')