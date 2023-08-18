#! /usr/bin/env python3 

import enum

class BugStatus(enum.Enum):
    
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commited = 2
    fix_released = 1
    
print(f'\nMember name -> {BugStatus.new.name}')
print(f'Member value -> {BugStatus.new.value}')