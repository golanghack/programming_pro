#! /usr/bin/env python3 

import sqlite3
import collections

db_filename = 'todo.db'

class Mode:
    
    def __init__(self):
        self.counter = collections.Counter()
        
    def step(self, value):
        print(f'step({value!r})')
        self.counter[value] += 1
        
    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print(f'finalize() -> {result!r} ({count} times)')
        return result
    
with sqlite3.connect(db_filename) as conn:
    conn.create_aggregate('mode', 1, Mode)
    
    cursor = conn.cursor()
    cursor.execute(
        """ 
        select mode(deadline) from task 
        where project = 'pymotw'
        """
    )
    row = cursor.fetchone()
    print('mode(deadline) is -> ', row[0])