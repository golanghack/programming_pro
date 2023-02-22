#! /usr/bin/env python3 

import pathlib 
import tempfile

with tempfile.TemporaryDirectory() as directory:
    the_dir = pathlib.Path(directory)
    print(the_dir)
    a_file = the_dir / 'a_file.txt'
    a_file.write_text('Hello.')
    
print('Directory exists after? ', the_dir.exists())
print('Contents after -> ', list(the_dir.glob('*')))