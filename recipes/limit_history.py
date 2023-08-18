#! /usr/bin/env python3 

""" 
Problem
You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.
from collections import deque
""" 

from collections import deque

def search(lines: str, pattern: str, history: int=5) -> str:
    """Return same string with before string"""

    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('my_text.txt', encoding='utf-8') as file:
        for line, prevlines in search(file, 'my', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)