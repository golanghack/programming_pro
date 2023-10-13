#! /usr/bin/env python3 

import pickle
import sqlite3

db_filename = 'todo.db'

def adapter(obj):
    """Convertering data from memory to storage."""
    
    print(f'Adapter function -> adapter({obj})')
    return pickle.dumps(obj)

def converter(data):
    """Converter data from storage in memory."""
    
    print(f'Converter function -> converter({data!r})')
    return pickle.loads(data)

class MyObj:
    
    def __init__(self, arg):
        self.arg = arg
        
    def __str__(self) -> str:
        return f'MyObj({self.arg!r})'
    
# registration
sqlite3.register_adapter(MyObj, adapter)
sqlite3.register_converter('MyObj', converter)

# create objects for saving.
# use list of tuples
to_save = [
    (MyObj('this is a value to save'),),
    (MyObj(45),),
]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_COLNAMES) as conn:
    # create table with 'text'
    conn.execute(""" 
                 create table if not exists obj2 (
                     id integer primary key autoincrement not null, 
                     data text
                     )
                     """)
    cursor = conn.cursor()
    
    # insert 
    cursor.executemany('insert into obj2 (data) values (?)', to_save)
    
    # request objects 
    cursor.execute('select id, data as "pickle [MyObj]" from obj2',)
    
    for obj_id, obj in cursor.fetchall():
        print('Retrieved -> ', obj_id, obj)
        print('with type', type(obj))
        print()
    