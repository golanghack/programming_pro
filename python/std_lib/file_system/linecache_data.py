#! /usr/bin/env python3 

import os 
import tempfile

lorem = ''' 
Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
Quaerat mollitia magnam aut excepturi neque quidem beatae 
eos quia dolores nulla molestiae ratione aliquid fuga architecto maiores 
repudiandae placeat, corrupti consectetur!

Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
Culpa consequuntur dignissimos ut reiciendis laborum voluptates 
officiis soluta non dolor accusamus. Voluptatem tempore dolore 
nihil facilis earum perspiciatis, itaque perferendis omnis.

Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
Corporis quae itaque doloribus eveniet fugiat ex! Soluta quo 
consequatur tempora nostrum sequi commodi natus earum molestias, 
accusamus at dolorem, libero magnam.
'''
def make_tempfile() -> str:
    """Create tempfile and return name of tempfile."""
    
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, 'wt') as my_file:
        my_file.write(lorem)
    return temp_file_name

def cleanup(filename: str) -> None:
    os.unlink(filename)
    
    