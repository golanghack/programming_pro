#! /usr/bin/env python3 

import enum 

BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_committed in_prigress'
           'wont_fix invalid incomplete new'),
)

print(f'Member -> {BugStatus.new}')
print('\nAll memebers -> ')
for status in BugStatus:
    print(f'{status.name:15} = {status.value}')