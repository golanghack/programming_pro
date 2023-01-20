#! /usr/bin/env python3 

import re 

text_pattern: str = 'this'
text: str = 'Does this text mathc the pattern?'

_match = re.search(text_pattern, text)

start = _match.start()
end = _match.end()

if __name__ == '__main__':
    print(f"""Found -> "{_match.re.pattern}"\n in "{_match.string}"\n from {start} to {end} ("{text[start:end]}")""")