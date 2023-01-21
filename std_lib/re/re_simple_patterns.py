#! /usr/bin/env python3 

import re 

def test_patterns(text: str, patterns: list) -> None:
    """Get text and list of patterns as arguments
    find all occurences every pattern in text and output results in stdout.
    """
    
    for pattern, description in patterns:
        print(f'<<<--"{pattern}" <-> ({description})-->>>\n')
        print(f'<<<-- "{text}"')
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            substring = text[start:end]
            backslashes = text[:start].count('\\')
            prefix = '.' * (start + backslashes)
            print(f'<<<-- {prefix} "{substring}" -->>>')
        print()
    return

if __name__ == '__main__':
    test_patterns('abbbabbbabbbabbabaaaaabaaaabbbabbbabbabbabababbabababbbaaa', [('ab', "'a', followed by 'b'"),]) 