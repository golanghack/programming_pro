#! /usr/bin/env python3 

import re 
import sqlite3

db_filename = 'todo.db'

def regex(pattern: str, input_data: str) -> bool:
    return bool(re.match(pattern, input_data))

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.create_function('regexp', 2, regex)
    cursor = conn.cursor()
    
    pattern = '.*[wW]rite [aA]bout.*'
    
    cursor.execute(
        """ 
        select id, priority, details, status, deadline from task
        where details regexp :pattern 
        order by deadline, priority
        """,
        {'pattern': pattern},
    )
    
    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print(f'{task_id:2d} [{priority:d}] {details:<25} [{status:<8}] ({deadline})')
