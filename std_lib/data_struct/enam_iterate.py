#! /usr/bin/env python3

import enum
from enam_create import BugStatus

for status in BugStatus:
    print(f'{status.name:15} = {status.value}')