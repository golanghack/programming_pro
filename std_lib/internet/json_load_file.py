#! /usr/bin/env python3 

import io
import json

file = io.StringIO('[{"a": "A", "c": 4.0, "b": [3, 5]}]')
print(json.load(file))