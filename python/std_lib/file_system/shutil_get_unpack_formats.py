#! /usr/bin/env python3 

import shutil

for format_, exts, descr in shutil.get_unpack_formats():
    print(f'{format_:<5} -> {descr}, names ending in {exts}')

