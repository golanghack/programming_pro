#! /usr/bin/env python3 

import pytest
from cards import Card

@pytest.fixture(params=['done', 'in prog', 'todo'])
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    c = Card('srite a book', state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
    