#! /usr/bin/env python3 

import cards
import pytest

def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()