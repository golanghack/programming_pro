#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GZIP MANAGER-->"""

import gzip

class GzipManager:
    
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.fh = gzip.open(self.filename, self.mode)
        return self.fh 
    
    def __exit__(self, *ignore):
        self.fh.close()