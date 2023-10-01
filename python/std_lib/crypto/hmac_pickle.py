#! /usr/bin/env python3 

import hashlib
import hmac
import io 
import pickle

def make_digest(message: str):
    """Return digest from message."""

    hash_str = hmac.new(
        b'secret', 
        message, 
        hashlib.sha256,
    )
    return hash_str.hexdigest().encode('utf-8')

class SimpleObject:
    """Creating and using testing digest before serialization."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

# imitation record socket with buffer
out_sock = io.BytesIO()

# record correct object in thread
# digest \n lenght \n pickle
obj = SimpleObject('digest matches')
picked_data = pickle.dumps(obj)
digest = make_digest(picked_data)

header = b'%s %d\n' % (digest, len(picked_data))
print(f'WARNING -> {header}')
out_sock.write(header)
out_sock.write(picked_data)

# record uncorrect object to thread
obj = SimpleObject('digest does not match')
picked_data = pickle.dumps(obj)
digest = make_digest(b'not the picked data at all')
header = b'%s %d\n' % (digest, len(picked_data))
print(f'WARNING -> {header}')
out_sock.write(header)
out_sock.write(picked_data)

out_sock.flush()

# imitation readable socket 
in_sock = io.BytesIO(out_sock.getvalue())

# reading 
while True:
    first_line = in_sock.readline()
    if not first_line:
        break
    incoming_digest, incoming_lenght = first_line.split(b' ')
    incoming_lenght = int(incoming_lenght.decode('utf-8'))

    print('\nREAD -> ', incoming_digest, incoming_lenght)

incoming_picked_data = in_sock.read(incoming_lenght)

actual_digest = make_digest(incoming_picked_data)
print('ACRUAL -> ', actual_digest)

if hmac.compare_digest(actual_digest, incoming_digest):
    obj = pickle.loads(incoming_picked_data)
    print('OK -> ', obj)
else:
    print('WARNING -> DATA CORRUPTION')

