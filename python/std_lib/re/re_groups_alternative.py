#! /usr/bin/env python3 

from re_simple_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [
        (r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
        (r'a((a|b)+)', 'a then seq. of [ab]')
    ],
)