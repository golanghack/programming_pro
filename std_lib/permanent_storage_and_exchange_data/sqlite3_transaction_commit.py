#! /usr/bin/env python3 

import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print('  ', name)
        
with sqlite3.connect(db_filename) as conn1:
    print('Before changes -> ')
    show_projects(conn1)
    
    # insert 
    cursor1 = conn1.cursor()
    cursor1.execute("""insert or ignore into project (name, description, deadline)
                    values ('virtualenvwrapper', 'Virtualenv Extensions', '2023-04-01')
                    """)
    
    print('\nAfter changes in conn1 -> ')
    show_projects(conn1)
    
# selecting from another connection
print('\nBefore commit -> ')
with sqlite3.connect(db_filename) as conn2:
    show_projects(conn2)
# committing and select
conn1.commit()
print('\After commit -> ')
with sqlite3.connect(db_filename) as conn3:
    show_projects(conn3)
    