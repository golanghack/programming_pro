#! /usr/bin/env python3

import enum
from enum_create import BugStatus

for status in BugStatus:
    print(f'{status.name:15} = {status.value}')