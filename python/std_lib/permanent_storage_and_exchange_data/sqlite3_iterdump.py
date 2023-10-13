#! /usr/bin/env python3 

import sqlite3

schema_filename = 'todo_schema.sql'

with sqlite3.connect(':memory:') as conn:
    conn.row_factory = sqlite3.Row
    
print('Creating schema -> ')
with open(schema_filename, encoding='utf-8') as file_:
    schema = file_.read()

conn.executescript(schema)

print('Inserting initial data')
conn.execute("""insert into project (name, description, deadline) 
             values ('pymotw', 'Python module of the week', '2023-09-09')
             """)

data = [
    ('write about select', 'done', '2023-09-09','pymotw'), 
    ('write about random', 'done', '2023-08-09','pymotw'),
    ('write about dict', 'active', '2023-06-09','pymotw'),
    ('write about select', 'waiting', '2023-11-09','pymotw'),   
]

conn.executemany("""insert into task (details, status, deadline, project)
                 values (?, ?, ?, ?)
                 """, data)

print('Dumping -> ')
for text in conn.iterdump():
    print(text)