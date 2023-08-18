#! /usr/bin/env python3 

from unittest.mock import MagicMock
import pytest 

def connect_to_db(host: str, ns: str) -> MagicMock:
    return MagicMock()

class Series:
    
    def __init__(self, *args):
        pass
    
class Actors:
    
    def __init__(self, *args):
        pass
    
    
@pytest.fixture(scope='session')
def db() -> None:
    db = connect_to_db('localhost', 'test')
    db.create_table(Series)
    db.create_table(Actors)
    yield db 
    db.prune()
    db.disconnect()
    
@pytest.fixture(scope='function')
def transaction(db) -> None:
    transaction = db.start_transaction()
    yield transaction
    transaction.rollback()
    
def test_insert(transaction) -> None:
    transaction.add(Series('The Office', 2005, 8,8))
    assert transaction.find(name='The Office') is not None