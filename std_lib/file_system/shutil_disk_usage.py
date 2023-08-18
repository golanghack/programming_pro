#! /usr/bin/env python3 

import shutil 

TOTAL_B, USED_B, FREE_B = shutil.disk_usage('.')

#gigibite
GIB = 2 ** 30

# gigabite
GB = 10 ** 9 

print(f'TOTAL -> {TOTAL_B / GB:6.2f} GB {TOTAL_B / GIB} GiB')
print()
print(f'USED -> {USED_B / GB:6.2f} GB {USED_B / GIB:6.2f} GiB')
print()
print(f'FREE -> {FREE_B / GB:6.2f} GB {FREE_B / GIB:6.2f} GiB')
