#! /usr/bin/env python3 

from re_simple_patterns import test_patterns

test_patterns(
    'abbabbaaabbba',
    [
        ('[ab]', 'either a or b'),
        ('a[ab]+', 'a followes by 1 or more a or b'),
        ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')
    ],
)