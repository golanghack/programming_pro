#! /usr/bin/env python3 

from enum_create import BugStatus

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality -> ', 
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identity -> ',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value -> ')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print(f' Cannot sort -> {err}')