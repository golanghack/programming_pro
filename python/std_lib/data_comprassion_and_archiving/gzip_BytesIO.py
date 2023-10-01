#! /usr/bin/env python3 

import gzip 
from io  import BytesIO
import binascii

uncompressed_data = b'The same line, over and over.\n' * 10
print('UNCOMPRESSED -> ', len(uncompressed_data))
print(uncompressed_data)

buf = BytesIO()
with gzip.GzipFile(mode='wb', fileobj=buf) as file_:
    file_.write(uncompressed_data)
    
compressed_data = buf.getvalue()
print('COMPRESSED -> ', len(compressed_data))
print(binascii.hexlify(compressed_data))

inbuffer = BytesIO(compressed_data)
with gzip.GzipFile(mode='rb', fileobj=inbuffer) as file_:
    reread_data = file_.read(len(uncompressed_data))
    
print('\nREREAD -> ', len(reread_data))
print(reread_data)