#! /usr/bin/env python3 
from cards import Card

def test_to_dict():
    """Given a Card object with known contents
        when we call to_dict() on the object 
        then the result will be a dictonary with known content
    """
    
    c1 = Card('something', 'brian', 'todo', 123)
    c2 = c1.to_dict()
    c2_expected = {
        'summary': 'something', 
        'owner': 'brian', 
        'state': 'todo', 
        'id': 123,
    }
    assert c2 == c2_expected
    
    