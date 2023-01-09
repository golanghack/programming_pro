#! /usr/bin/env python3 
from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture(scope='session')
def db():
    """CardsDB object connected to a temporary database."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db 
        db.close()
        
@pytest.fixture(scope='function')
def cards_db(db):
    """CardsDB object that`s empty."""
    db.delete_all()
    return db 

@pytest.fixture(scope='session')
def some_cards():
    """List of different Card objects."""
    return [
        cards.Card('write book', 'Brian', 'done'),
        cards.Card('edit book', 'Katie', 'done'),
        cards.Card('write 2nd edition', 'Brian', 'todo'),
        cards.Card('edit 2nd edition', 'Katie', 'todo'),
    ]


