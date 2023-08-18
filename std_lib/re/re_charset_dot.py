#! /usr/bin/env python3 

from re_simple_patterns import test_patterns

test_patterns(
    'abbaabbbaa',
    [
        ('a.', 'a followed by any one character'),
        ('b.', 'b followed by eny one character'),
        ('a.*b', 'a followes by anything, ending in b'),
        ('a.*?b', 'a followed by enything, ending in b')
    ],
)