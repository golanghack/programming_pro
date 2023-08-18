#! /usr/bin/env python3 

import codecs
import sqlite3

db_filename = 'todo.db'

def encrypt(s: str) -> str:
    print(f'Encrypting {s!r}')
    return codecs.encode(s, 'rot-13')

def decrypt(s: str) -> str:
    print(f'Decrypting -> {s!r}')
    return codecs.encode(s, 'rot-13')

with sqlite3.connect(db_filename) as conn:
    conn.create_function('encrypt', 1, encrypt)
    conn.create_function('decrypt', 1, decrypt)
    cursor = conn.cursor()
    
# row 
print('Original values -> ')
query = 'select id, details from task'
cursor.execute(query)

for row in cursor.fetchall():
    print(row)
    
print('\nEncrypting -> ')
query = 'update task set details = encrypt(details)'
cursor.execute(query)

print('\nRaw enctrypted values -> ')
query = 'select id, details from task'
cursor.execute(query)

for row in cursor.fetchall():
    print(row)
    
print('\nDecryptins in query -> ')
query = 'select id, decrypt(details) from task'
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
    
print('\nDecrypting -> ')
query = 'update task set details = decrypt(details)'
cursor.execute(query)