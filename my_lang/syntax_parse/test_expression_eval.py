#! /usr/bin/env python3 

"""Test expression_eval function"""

from .expression_eval import prefetch_eval
from .parse_express import parse_express


def test_expression_eval():
    def intro_func(custom_string):
        return prefetch_eval(parse_express(list(custom_string), len(custom_string) - 1))
    
    assert intro_func('1') == 1
    assert intro_func('(+1 3)') == 4
    assert intro_func('(? (lt 1 3) "yes" "no")') == 'yes'
    assert intro_func('(print 1 2 3)') is None
