#! /usr/bin/env python3 

import enum

BugStatus = enum.Enum(
    value='BugStatus',
    names=[
        ('new', 7), 
        ('incomplete', 6),
        ('invalid', 5),
        ('wont_fix', 4),
        ('in_progress', 3),
        ('fix_commited', 2),
        ('fix_released', 1),
    ],
)

print('All members -> ')
for status in BugStatus:
    print(f'{status.name:15} = {status.value}')