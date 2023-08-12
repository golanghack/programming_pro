#! /usr/bin/env python3 

import getpass
import sys 

password = getpass.getpass(stream=sys.stderr)
print(f'Entered -> {password}')