#! /usr/bin/env python3 

import sqlite3
import sys 

db_filename = 'todo.db'

sql = """select id, details, deadline from task"""

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    
    for col in ['id', 'details', 'deadline']:
        print(f'{col:<8} {row[col]!r:<25} {type(row[col])}')
    return


print('Without type detection -> ')
with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)
    
print('\nWith type detection -> ')
with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES,) as conn:
    show_deadline(conn)