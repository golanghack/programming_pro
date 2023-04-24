#! /usr/bin/env python3 

from urllib.parse import urlencode

query_args = {
    'foo': ['foo1', 'foo2',],
}
print('Single -> ', urlencode(query_args))
print('Sequence -> ', urlencode(query_args, doseq=True))