#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--FASAD-->"""

import contextlib
import gzip
import os
import re 
import string
import tarfile
import zipfile


class Archive:
    """Main class for managed archives -> Fasad"""
    
    def __init__(self, filename: str) -> None:
        self._names = None
        self._unpack = None
        self._file = None
        self.filename = filename
        
    @property
    def filename(self) -> str:
        return self.__filename
    
    @filename.setter
    def filename(self, name: str) -> None:
        self.close()
        self.__filename = name
        
    def close(self) -> None:
        if self._file is not None:
            self._file.close()
        self._names = self._unpack = self._file = None
        
    def names(self) -> list:
        """Return list of files in archive. If archive didnt open -> open"""
        
        if self._file is None:
            self._prepare()
        return self._names()
    
    def unpack(self) -> None:
        """Take out all names from archive"""
        
        if self._file is None:
            self._prepare()
        self._unpack()
        
    def _prepare(self) -> None:
        """Preparing methods for format archive"""
        
        if self.filename.endswith(('.tar.gz', '.tar.bz2', '.tzr.xz', '.zip')):
            self._prepare_tarball_or_zip()
        if self.filename.endswith('.gz'):
            self._prepare_gzip()
        else:
            raise ValueError(f'unreadable: {self.filename}')
        
    def _prepare_tarball_or_zip(self) -> None:
        """Create into function extracting
        """
        def safe_extractall():
            """Callback -> trying save or unsave"""
            
            unsafe = []
            for name in self.names():
                if not self.is_safe(name):
                    unsafe.append(name)
            if unsafe:
                raise ValueError(f'unsafe to unpack -> {unsafe}')
            self._file.extractall()
            
        if self.filename.endswith('.zip'):
            self._file = zipfile.ZipFile(self.filename)
            self._names = self._file.namelist
            self._unpack = safe_extractall
        else:
            suffix = os.path.splitext(self.filename)[1]
            self._file = tarfile.open(self.filename, 'r:' + suffix[1:])
            self._names = self._file.getnames
            self._unpack = safe_extractall
            
            
    def _prepare_gzip(self) -> None:
        """Writing open file"""
        
        self._file = gzip.open(self.filename)
        filename = self.filename[:-3]
        self._names = lambda: [filename]
        def extractall():
            with open(filename, 'wb') as file:
                file.write(self._file.read())
        self._unpack = extractall
        
    def is_safe(self, filename: str) -> bool:
        """Testing all filenames """
        
        return not (filename.startswith(('/', '\\')) or 
                    (len(filename) > 1 and 
                     filename[1] == ':' and 
                     filename[0] in string.ascii_letters) or 
                    re.search(r'[.][.][/\\]', filename))
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        self.close()
        
    def __str__(self) -> str:
        return f'{self.filename} ({self._file is not None}'
    
if __name__ == '__main__':
    import errno
    import os 
    import shutil
    import tempfile
    
    from_path = os.path.dirname(os.path.abspath(__file__))
    to_path = os.path.join(tempfile.gettempdir(), 'unpack')
    
    try:
        os.makedirs(to_path)
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise
    
    zip_filename = os.path.join(to_path, 'tezt.zip')
    zip_names = ['Bag1.py', 'Bag2.py', 'Bag3.py']
    
    tar_filename = os.path.join(to_path, 'test.tar.gz')
    tar_names = ['genome1.py', 'genome2.py', 'genome3.py']
    
    gz_filename = os.path.join(to_path, 'hello.pyw.gz')
    gz_name = 'hello.pyw'
    
    file = None
    
    try:
        file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
        for name in zip_names:
            file.write(name)
    finally:
        if file is not None:
            file.close()
    
    file = None
    
    try:
        file = tarfile.open(tar_filename, 'w:gz')
        for name in tar_names:
            file.add(name)
    finally:
        if file is not None:
            file.close()
            
    file = None
    
    try:
        file = gzip.open(gz_filename, 'w')
        with open(gz_name, 'rb') as infile:
            file.write(infile.read())
    finally:
        if file is not None:
            file.close()
            
            
    os.chdir(to_path)
    with Archive(zip_filename) as archive:
        print(archive.names())
        assert archive.names() == zip_names
        archive.unpack()
        
        archive.filename = tar_filename
        print(archive.names())
        assert archive.names() == tar_names
        archive.unpack()
        
        archive.filename = gz_filename
        archive.unpack()
    
    shutil.rmtree(to_path)