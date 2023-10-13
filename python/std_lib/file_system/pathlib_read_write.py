#! /usr/bin/env python3 

import pathlib

my_file = pathlib.Path('example.txt')
my_file.write_bytes('This is the my content'.encode('utf-8'))

with my_file.open('r', encoding='utf-8') as handle:
    print(f'read from open() -> {handle.read()!r}')

print(f'read_text() -> {my_file.read_text("utf-8")}')