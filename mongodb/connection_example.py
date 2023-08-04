#! /usr/bin/env python3 

"""A connection axample with MongoDB""" 

import pymongo
from pymongo.errors import ConnectionFailure
import sys 


def main():
    """Connect""" 

    try:
        client = pymongo.MongoClient('localhost', 27017)
        print('Success!')
    except ConnectionFailure as err:
        sys.stderr.write(f'Could not connect to ModngoDB -> {err}')
        sys.exit(1)
if __name__ == '__main__':
    main()