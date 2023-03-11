#! /usr/bin/env python3 

import datetime 
import zipfile

def print_info(archive_name: str) -> None:
    with zipfile.ZipFile(archive_name) as z_file:
        for info in z_file.infolist():
            print(info.filename)
            print('Comment -> ', info.comment)
            mod_data = datetime.datetime(*info.date_time)
            print('Modified -> ', mod_data)
            if info.create_system == 0:
                system = 'Windows'
            elif info.create_system == 3:
                system = 'Unix'
            else:
                system = 'UNKNOWN'
            print('System -> ', system)
            print('ZIP version -> ', info.create_version)
            print('Cmpressed -> ', info.compress_size, ' bytes')
            print('Uncompressed -> ', info.file_size, ' bytes')
            print()
            
if __name__ == '__main__':
    print_info('example.zip')