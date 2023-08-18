#! /usr/bin/env python3 

import sqlite3

db_filename = 'todo.db'

def authorizer(action, table, column, sql_location, ignore):
    print(f'\nauthorizer({action}, {table}, {column}, {sql_location}, {ignore})')
    # default
    response = sqlite3.SQLITE_OK
    
    if action == sqlite3.SQLITE_SELECT:
        print('requesting permission to run a select statement')
        response = sqlite3.SQLITE_OK
        
    elif action == sqlite3.SQLITE_READ:
        print(f'requesting access to column{table}.{column} from {sql_location}')
        if column == 'details':
            print('ignoring dertails column')
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priority':
            print('preventing access to priority column')
            response = sqlite3.SQLITE_DENY
    return response

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer)
    
    print('Using SQLITE_IGNORE to mask a column value -> ')
    cursor = conn.cursor()
    cursor.execute(
        """ 
        select id, details from task 
        where project = 'pymotw'
        """
    )
    
    for row in cursor.fetchall():
        print(row['id'], row['details'])
        
    print('\nUsing SQLITE_DENY to deny access to a column -> ')
    cursor.execute(
        """
        select id, priority from task where project = 'pymotw' 
        """
    )
    
    for row in cursor.fetchall():
        print(row['id'], row['details'])