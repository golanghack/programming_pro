#! /usr/bin/env python3 

import codecs
from codecs_invertcaps_charmap import encoding_map

text = 'pi -> \u03c0'

for error in ['ignore', 'replace', 'strict']:
    try:
        encoded = codecs.charmap_encode(text, error, encoding_map)
    except UnicodeEncodeError as err:
        encoded = str(err)
    print(f'{error:7} -> {encoded}')