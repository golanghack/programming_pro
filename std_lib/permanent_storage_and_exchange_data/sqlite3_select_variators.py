#! /usr/bin/env python3 

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
                   SELECT name, description, deadline project 
                   WHERE name = 'pymotw'
                   """)
    name, description, deadline = cursor.fetchone()
    
    print(f'Project details for {description} ({name})\n due {deadline}')
    
    cursor.execute("""
                   SELECT id, priority, details, status, deadline FROM task 
                   WHERE project = 'pymotw' ORDER BY deadline
                   """)
    
    print('\nNext 5 tasks -> ')
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row 
        print(f'{task_id:2d} [{priority:d}] {details:<25} [{status:<8}] ({deadline}) ')