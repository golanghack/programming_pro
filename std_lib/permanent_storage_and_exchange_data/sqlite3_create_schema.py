#! /usr/bin/env python3 

import os 
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename,  encoding='utf-8') as file_:
            schema = file_.read()
            conn.executescript(schema)
        
        print('Inserting initial data')
        
        conn.executescript(""" 
                           INSERT INTO project (name, description, deadline)
                           VALUES ('pymotw', 'Python Module os the Week', 
                           '2016-11-01');
                           
                           INSERT INTO task (details, status, deadline, project)
                           VALUES ('write about select', 'done', '2023-04-25', 'pymotw');
                           
                           INSERT INTO task (details, status, deadline, project)
                           VALUES ('write about random', 'waiting', '2023-08-22', 'pymotw');
                           
                           INSERT INTO task (details, status, deadline, project)
                           VALUES ('write about sqlite3', 'active', '2023-07-31', 'pymotw');
                           
                           """)
    else:
        print('Database exists, assume schema does, too.')   
        