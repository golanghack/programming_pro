import pytest
from cards import Card

@pytest.mark.skip(reason='Card doesn`t support < comparison yet')
def test_less_than():
    c1 = Card('a task')
    c2 = Card('a task')
    assert c1 < c2 