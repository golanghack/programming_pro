#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--BINARY RECORD FILE SIMPLE VERSION-->
   <--THE UTILIT FOR WRITING BINARY FILES-->
   
>>> import shutil
>>> import sys

>>> S = struct.Struct("<15s")
>>> fileA = os.path.join(tempfile.gettempdir(), "fileA.dat")
>>> fileB = os.path.join(tempfile.gettempdir(), "fileB.dat")
>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> brf = BinaryRecordFile(fileA, S.size)
>>> for text in ("Alpha", "Bravo", "Charlie", "Delta",
...        "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
...        "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
...        "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
...        "Whisky", "X-Ray", "Yankee", "Zulu"):
...    brf.append(S.pack(text.encode("utf8")))
>>> assert len(brf) == 26
>>> brf.append(S.pack(b"Extra at the end"))
>>> assert len(brf) == 27
>>> shutil.copy(fileA, fileB)
>>> del brf[12]
>>> del brf[0]
>>> del brf[24]
>>> assert len(brf) == 24, len(brf)
>>> brf.close()

>>> if ((os.path.getsize(fileA) + (3 * S.size)) !=
...        os.path.getsize(fileB)):
...    print("FAIL#1: expected file sizes are wrong")
...    sys.exit()

>>> shutil.copy(fileB, fileA)
>>> if os.path.getsize(fileA) != os.path.getsize(fileB):
...    print("FAIL#2: expected file sizes differ")
...    sys.exit()

>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

"""

import os 
import struct
import tempfile


class BinaryRecordFile:
    
    def __init__(self, 
                 filename: str, 
                 record_size: bytearray, 
                 auto_flush: bool=True):
        """A random access binary file that behaves rather like a list
        with each item a bytes or bytesarray object of record_size.
        """
        
        self.__record_size = record_size
        mode = 'w+b' if not os.path.exists(filename) else 'r+b'
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush
        
    @property
    def record_size(self) -> bytearray:
        """The size of each item"""
        
        return self.__record_size
    
    @property
    def name(self) -> None:
        """Flush writes to disk. Done automatically if auto_flush is True"""
        
        self.__fh.flush()
        
    
    def close(self) -> None:
        """Close file"""
        
        self.__fh.close()
        
    def append(self, record: bytes) -> None:
        """Adds a new record"""
        
        assert isinstance(record, (bytes, bytearray)), 'binary data required'
        assert len(record) == self.record_size, f'record must by exactly {self.record_size} bytes'
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()
            
    def __setitem__(self, index: int, record: bytearray) -> None:
        """Sets the item at position index to be the given record
            The index position can be beyond the current end of the file.
        """
        
        assert isinstance(record, (bytes, bytearray)), 'binary data required'
        assert len(record) == self.record_size, f'record must be exactly {self.record_size} bytes'
        self.__seek_to_index(index)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()
            
    def __getitem__(self, index: int) -> int:
        """Returns the item at the given index position
        If there is no item at the given position, raises an
        IndexError exception.
        If the item at the given position has been deleted returns
        None.
        """
        
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)
    
    def __seek_to_index(self, index: int) -> None:
        """Searching on index"""
        
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.record_size
        if offset >= end:
            raise IndexError(f'no record at index position {index}')
        self.__fh.seek(offset)
        
        
    def __delitem__(self, index: int) -> None:
        """Deletes the item at the given index position and moves the
        following records up.
        """
        
        lenght = len(self)
        for following in range(index + 1, lenght):
            self[index] = self[following]
            index += 1
        self.__fh.truncate((lenght - 1) * self.record_size)
        self.__fh.flush()
        
    
    def __len__(self) -> float:
        """The number number of records"""
        
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.record_size
    
    if __name__ == '__main__':
        import doctest
        doctest.testmod()      
        
    