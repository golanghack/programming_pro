#! /usr/bin/env python3 

import sqlite3
import sys 
import threading
import time 

db_filename = 'todo.db'
# mode auto fixing
isolation_level = None

def reader(conn):
    print('Starting thread -> ')
    try: 
        cursor = conn.cursor()
        cursor.execute('select * from task')
        cursor.fetchall()
        print('result fetched')
    except Exception as err:
        print('!!!ERROR!!!', err)
        
if __name__ == '__main__':
    with sqlite3.connect(db_filename, isolation_level=isolation_level, ) as conn:
        t = threading.Thread(name='Reader 1', target=reader, args=(conn,),)
        
        t.start()
        t.join()