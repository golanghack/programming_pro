#! /usr/bin/env python3

from cards import Card

def test_finish(cards_db):
    for i in [
        Card('write a book', state='done'),
        Card('second edition', state='in prog'),
        Card('create a course', state='todo'),
    ]:
        index = cards_db.add_card(i)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == 'done'