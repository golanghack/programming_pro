#! /usr/bin/env python3 
from pathlib import Path
from tempfile import TemporaryDirectory
import faker
import cards
from cards import Card
import pytest

def db_scope(fixture_name, config):
    if config.getoption('--func-db', None):
        return 'function'
    return 'session'

@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temporary database."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db 
        db.close()
        
@pytest.fixture(scope='function')
def cards_db(session_cards_db, request, faker):
    """CardsDB object that`s empty."""
    db = session_cards_db
    db.delete_all()
    faker.seed_instance(101)
    m = request.node.get_closest_marker('num_cards')
    if m in len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(Card(summary=faker.sentence(), owner=faker.first_name()))
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

def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)
    for c in some_cards:
        cards_db.add_card(c)
    assert cards_db.count() == expected_count
    
@pytest.fixture(scope='function')
def non_empty_db(cards_db, some_cards):
    """CardsDB object that`s populated with 'some_cards'"""
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db

def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0

def pytest_addoption(parser):
    parser.addoption(
        '--func-db', 
        action='store_true', 
        default=False, 
        help='new db for each test',
    )
        
        
