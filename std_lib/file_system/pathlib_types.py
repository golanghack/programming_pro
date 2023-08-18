#! /usr/bin/env python3 

import itertools
import os 
import pathlib

root = pathlib.Path('test_files')

# remove objects created before
if root.exists():
    for f in root.iterdir():
        f.unlink()
else:
    root.mkdir()
    
# test files creating 
(root / 'file').write_text('This is a regular file', encoding='utf-8')
(root / 'symlink').symlink_to('file')
os.mkfifo(str(root / 'fifo'))

# testing types of files 
to_snanning = itertools.chain(
    root.iterdir(), 
    [pathlib.Path('/dev/disk0'), 
     pathlib.Path('/dev/console')],
)

hight_fmt = '{:18s}' + ('  {:>5}' * 6)
print(hight_fmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block', 'Character'))
print()

low_fmt = '{:20s}  ' + ('{!r:>4}  ' * 6)
for f in to_snanning:
    print(low_fmt.format(
        str(f), 
        f.is_file(), 
        f.is_dir(),
        f.is_symlink(), 
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))