#! /usr/bin/env python3 

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    
    cursor.execute(""" 
                   SELECT id, priority, details, deadline FROM task
                   WHERE project = 'pymotw'
                   """)
    
    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row 
        print(f'{task_id:2d} [{priority:d}] {details:<25} [{status:<8}]({deadline})')