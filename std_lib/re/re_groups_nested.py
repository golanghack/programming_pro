#! /usr/bin/env python3 

from re_simple_patterns_groups import test_patterns


test_patterns(
    'abbaabbba', 
    [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
)