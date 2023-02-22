#! /usr/bin/env python3 

import shutil

for format_, description in shutil.get_archive_formats():
    print(f'{format_:<5} -> {description}')