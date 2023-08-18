#! /usr/bin/env python3 
"""Insert example"""

import pymongo
from pymongo.errors import ConnectionFailure
from datetime import datetime
import sys 

def main():
    try:
        client = pymongo.MongoClient('localhost', 27017)
    except ConnectionFailure as err:
        sys.stderr.write(f'Could not connect with mongo -> {err}')
        sys.exit(1)
    
    handle = client['mydb']
    assert handle.client == client
    
    user_doc = {
        'username': 'test_one', 
        'firstname': 'test_one',
        'surname': 'test_one',
        'dateofbirht': datetime(1985, 4, 12),
        'email': 'test_one@gmail.com',
        'score': 0
    }
    handle.users.insert(user_doc, safe=True)
    print('Success inserting')

if __name__ == '__main__':
    main()