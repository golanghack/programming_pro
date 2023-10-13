#! /usr/bin/env python3 
"""Insert example"""

import pymongo
from pymongo.errors import ConnectionFailure
import sys 
from user_doc import user_doc
from user_location import user_doc_location

def main():
    try:
        client = pymongo.MongoClient('localhost', 27017)
    except ConnectionFailure as err:
        sys.stderr.write(f'Could not connect with mongo -> {err}')
        sys.exit(1)
    
    handle = client['mydb']
    assert handle.client == client
    
    handle.users.insert_one(user_doc)
    print('Success inserting')

    # find
    user_doc_response = handle.users.find_one({"username": "foouser"})
    print(user_doc_response)

    # update 
    user_update = handle.users.update_one({"username":"foouser"},
                                {"$pull":{"emails": {"primary": {"$ne": True}}}})
    

    # create index
    index = handle.users.create_index([("first_name", pymongo.ASCENDING),
                                        "last_name", pymongo.ASCENDING],
                                        name="name_indexes")
    
    # drop index 
    dropping = handle.users.drop_index("name_indexes")

    # geoindex
    geolocation = handle.users.create_index(["user_location", pymongo.GEO2D])
    

if __name__ == '__main__':
    main()