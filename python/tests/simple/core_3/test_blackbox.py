#! /usr/bin/env python3 

from unittest.mock import MagicMock
import pytest

class BotFixture:
    """Creating Fixture for pytest and unittest"""
    
    def __init__(self) -> None:
        self.store = {'TEST': {'token': None}}
        
    def say(self, message: str) -> str:
        """Use MagicMock."""
        
        result = MagicMock()
        if message == 'hello':
            result.text = 'Hey, how can i help you?'
        elif message == 'my token is ABCDEFGKM':
            self.store['TEST']['token'] = 'ABCDEFGKM'
            result.text = 'OK, your token was saved.'
        else:
            assert False
        return result
    
@pytest.fixture
def bot() -> BotFixture:
    return BotFixture()

def test_hello(bot: BotFixture) -> None:
    reply = bot.say('hello')
    assert reply.text == 'Hey, how can i help you?'
    
def test_store_deploy_token(bot: BotFixture) -> None:
    assert bot.store['TEST']['token'] is None
    reply = bot.say('my token is ABCDEFGKM')
    assert reply.text == 'OK, your token was saved.'
    assert bot.store['TEST']['token'] == 'ABCDEFGKM'