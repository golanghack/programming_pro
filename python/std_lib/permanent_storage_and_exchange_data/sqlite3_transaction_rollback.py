#! /usr/bin/env python3 

import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print('  ', name)
        
with sqlite3.connect(db_filename) as conn:
    print('Before changes -> ')
    show_projects(conn)
    
    try:
        # insert 
        cursor = conn.cursor()
        cursor.execute("""delete from project where name = 'virtualenvwrapper'""")
        
        # show results 
        print('\nAfter delete -> ')
        show_projects(conn)
        
        # raise exception
        raise RuntimeError('simulated error')
    
    except Exception as err:
        # rollback
        print('ERROR -> ', err)
        conn.rollback()
print('\nAfter rollback -> ')
show_projects(conn)