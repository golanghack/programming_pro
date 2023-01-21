#! /usr/bin/env python3

from re_simple_patterns_groups import test_patterns

test_patterns(
    'abbaabbba', 
    [(r'a((a+)|(b+))','capturaing form'),
     (r'a((?:a+)|(?:b+))', 'noncapturing')],
)