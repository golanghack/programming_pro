#! /usr/bin/env python3 

import hashlib

def commit_hash(contents: list) -> list:
    """Return hash contents.
    :param -> contents -> list.
    :return -> list.
    """
    
    size = len(contents)
    print('content size', size)
    
    hash_contents = str(size) + '\n' + contents
    result = hashlib.sha1(hash_contents.encode('UTF-8')).hexdigest()
    print(result)
    return result[:8]

def test_commit_hash() -> None:
    contents = 'some text contents for commit'
    assert commit_hash(contents) == 'f1fc3293'