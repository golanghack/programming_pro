#! /usr/bin/env python3 

"""To get handle a mongo database"""

import pymongo
from pymongo.errors import ConnectionFailure
import sys 

def main():
    """Connect""" 

    try:
        client = pymongo.MongoClient('localhost', 27017)
    except ConnectionFailure as err:
        sys.stderr.write(f'Could not connect with mongo -> {err}')
        sys.exit(1)
    db_handle = client['mydb']

    assert db_handle.client == client
    print('Success')
if __name__ == '__main__':
    main()