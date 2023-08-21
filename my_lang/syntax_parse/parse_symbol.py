#! /usr/bin/env python3 

"""Reinclude numbers, string, symbols from strings"""

import json

def parse_symbol(string: str):
    try:
        return ['value', json.loads(string)]
    except json.JSONDecodeError:
        return string