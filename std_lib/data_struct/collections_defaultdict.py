#! /usr/bin/env python3 

import collections

def default_factory() -> str:
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print('d -> ', d)
print('foo -> ', d['foo'])
print('bar -> ', d['bar'])