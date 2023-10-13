#! /usr/bin/env python3 

import io 
import mimetypes
import os 
import tempfile
from urllib import request, response

class NFSFile:

    def __init__(self, tempdir, filename):
        self.tempdir = tempdir
        self.filename = filename

        with open(os.path.join(tempdir, filename), 'rb') as file:
            self.buffer = io.BytesIO(file.read())

    def read(self, *args):
        return self.buffer.read(*args)

    def readline(self, *args):
        return self.buffer.readline(*args)

    def close(self):
        print('\nNFSFile -> ')
        print(f'Unmounting {os.path.basename(self.tempdir)}')
        print(f'when {os.path.basename(self.filename)} is closed')

class FauxNFSHandler(request.BaseHandler):

    def __init__(self, tempdir):
        self.tempdir = tempdir
        super().__init__()

    def nfs_open(self, req):
        url = req.full_url
        directory_name, file_name = os.path.split(url)
        server_name = req.host
        
        print('FauxNFSHandler simulating mount -> ')
        print(f'Remote path -> {directory_name}')
        print(f'Server -> {server_name}')
        print(f'Local path -> {os.path.basename(tempdir)}')
        print(f'Filename -> {file_name}')
        local_file = os.path.join(tempdir, file_name)
        fp = NFSFile(tempdir, file_name)
        content_type = (
            mimetypes.guess_type(file_name)[0] or 'application/octet_stream'
        )
        stats = os.stat(local_file)
        size = stats.st_size
        headers = {
            'Content-Type': content_type, 
            "Content-length": size,
        }
        return response.addinfourl(fp, headers, req.get_full_url())

if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tempdir:
        # create conetnt tempfile 
        filename = os.path.join(tempdir, 'file.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Contents of file.txt')
        
        # create object permission for resources with NFS and registered for him
        # and use default
        opener = request.build_opener(FauxNFSHandler(tempdir))
        request.install_opener(opener)

        # open file use URL 
        resp = request.urlopen('nfs://remote_server/path/to/the/file.txt')
        
        print()
        print('Read contents -> ', resp.read())
        print('url -> ', resp.geturl())
        print('Headers -> ')
        for name, value in sorted(resp.info().items()):
            print(f'{name:<15} = {value}')
        resp.close()