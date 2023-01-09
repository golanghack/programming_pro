#! /usr/bin/env python3 

import cards
import pytest

def test_raises_with_info():
    match_regex = 'missing 1.*position argument'
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()

    