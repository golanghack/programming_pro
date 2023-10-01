#! /usr/bin/env python3

import re 

def test_patterns(text: str, patterns: list) -> None:
    """Get start text and list of patterns as arguments 
    find all intro every pattern in text and output results in stdout.
    """
    
    #searchin all pattern in text
    for pattern, description in patterns:
        print(f'{pattern!r} ({description})\n')
        print(f'{text!r}')
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            prefix = ' ' * (start)
            print(f"""
                  {prefix}{text[start:end]!r}{' ' * (len(text) - end)}
                  """, end=' ')
            print(match.groups())
            if match.groupdict():
                print(f'{" " * (len(text) - start)}{match.groupdict()}')
        print()
    return

