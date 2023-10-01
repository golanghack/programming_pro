#! /usr/bin/env python3 

import pickle
import sqlite3

db_filename = 'todo.db'

def adapter(obj):
    """Converts data from memory to data storage."""
    
    print(f'adapter({obj})\n')
    return pickle.dumps(obj)

def converter(data):
    """Converts data from storage to memory"""
    
    print(f'converter({data!r})\n')
    return pickle.loads(data)

class MyObj:
    
    def __init__(self, arg):
        self.arg = arg
        
    def __str__(self) -> str:
        return f'MyObj({self.arg!r})'
    
# regiter function
sqlite3.register_adapter(MyObj, adapter)
sqlite3.register_converter('MyObj', converter)

# create data for save
# recomandation uses list of tuples
# for sequence send method executemany() from sqlite3 
to_save = [
    (MyObj('this is a value to save'), ),
    (MyObj(45),),
]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # create table for MyObj
    conn.execute(""" 
                 create table if not exists obj (
                     id integer primary key autoincrement not null, 
                     data MyObj
                     )
                     """)
    
    cursor = conn.cursor()
    
    # insert objects in db
    cursor.executemany("""insert into obj (data) values (?)""", to_save)
    
    # query for saved objects in db 
    cursor.execute('select id, data from obj')
    
    for obj_id, obj in cursor.fetchall():
        print('Retrieved -> ', obj_id, obj)
        print('  with type -> ', type(obj))
        print()