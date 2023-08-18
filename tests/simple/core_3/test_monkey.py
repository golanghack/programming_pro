#! /usr/bin/env python3 

import getpass
import pytest

class AuthenticationError(RuntimeError):
    pass

def check_credentials(name: str, password: str) -> bool:
    """Testing credentials."""
    
    if password == 'wrong-pass':
        raise AuthenticationError('!!!ERROR!!! WRONG PASSWORD')
    return True

def user_login(name: str) -> bool:
    """Testing user login."""
    
    password = getpass.getpass()
    check_credentials(name, password)
    return True

def test_loggin_success(monkeypatch) -> None:
    monkeypatch.setattr(getpass, 'getpass', lambda: 'real-pass')
    assert user_login('test-user')
    
def test_login_wrong_password(monkeypatch) -> None:
    monkeypatch.setattr(getpass, 'getpass', lambda: 'wrong-pass')
    with pytest.raises(AuthenticationError, match='!!!ERROR!!! WRONG PASSWORD'):
        user_login('test-user')