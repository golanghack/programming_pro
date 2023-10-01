#! /usr/bin/env python3 

import pathlib 

my_path = pathlib.Path('touched')
my_path.touch()

print('exists before removing -> ', my_path.exists())

my_path.unlink()
print('exists after removing -> ', my_path.exists())