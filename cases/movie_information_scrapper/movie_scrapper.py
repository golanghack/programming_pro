#! /usr/bin/env python3 

import os 
import zipfile
import sys 
import argparse 

# cli 
parser = argparse.ArgumentParser()
parser.add_argument('-z', '--zippedfile', required=True, help='Zipped file')
args = vars(parser.parse_args())

# catching the user defined zip file 
zip_file = args['zippedfile']
filename = zip_file

# to check if the enetered zip file is present in the directory
if os.path.exists(zip_file) == False:
    sys.exit('No such file prresent in the directory')

# extract the zip file
def extract(zip_file: str) -> None:
    filename = zip_file.split('.zip')[0]
    if zip_file.endswith('.zip'):
        # will use this save the unzipped file in the current directory
        current_directory = os.getcwd()
        new_directory = current_directory + '/' + filename
        
        # logic to unzip the file 
        with zipfile.ZipFile(zip_file, 'r') as zip_obj:
            zip_obj.extractall(new_directory)
        print('Extract successfully')
    else:
        print('No zip file')

if __name__ == '__main__':
    extract(zip_file)