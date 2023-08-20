
from math_json_tree.json_mutator import math_mutator

def test_true_identity():
    """Test idetity"""

    assert math_mutator(9) == 9, 'identity'

def test_single_element():
    assert math_mutator(['+', 3]) == 3, 'single element'

def test_add():
    assert math_mutator(['+', 1, 1]) == 2, 'add two numbers'

def test_nested():
    assert math_mutator(['*', ['+', 5, 4], 2]) == 18