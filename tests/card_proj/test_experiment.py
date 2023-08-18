#! /usr/bin/env python3 

import cards
import pytest

def test_raises_with_info():
    match_regex = 'missing 1.*position argument'
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()
        
def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
    expected = 'missing 1 required position argument'
    assert expected in str(exc_info.value)

    