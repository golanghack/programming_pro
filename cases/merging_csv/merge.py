#! /usr/bin/env python3 

import glob
import pandas as pd 

extension = 'csv'
all_filenames = [i for i in glob.glob(f'*.{extension}')]

combined_csv = pd.concat([pd.read_csv(one_file) for one_file in all_filenames])
combined_csv.to_csv('combined_csv.csv', index=False, encoding='utf-8-sig')

