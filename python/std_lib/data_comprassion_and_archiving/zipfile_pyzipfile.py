#! /usr/bin/env python3 

import sys 
import zipfile

if __name__ == '__main__':
    with zipfile.PyZipFile('pyzipfile.zip', mode='w') as file:
        file.debug = 3 
        print('Adding python files')
        file.writepy('.')
    for name in file.namelist():
        print(name)
        
    print()
    sys.path.insert(0, 'pyzipfile.zip')
    import zipfile_pyzipfile
    print('Imported from -> ', zipfile_pyzipfile.__file__)