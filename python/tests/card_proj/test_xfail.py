import pytest
from cards import Card
import cards
from packaging.version import parse

@pytest.mark.xfail(
    parse(cards.__version__).major < 2,
    reason='Card < comparison not supported in 1.x',
)

def test_less_than():
    c1 = Card('a task')
    c2 = Card('b task')
    assert c1 < c2 
    
@pytest.mark.xfail(reason='!!!XPASS DEMO!!!')
def test_xpass():
    c1 = Card('a task')
    c2 = Card('a task')
    assert c1 == c2 
    
@pytest.mark.xfail(reason='strict demo', strict=True)
def test_strict():
    c1 = Card('a task')
    c2 = Card('a task')
    assert c1 == c2 