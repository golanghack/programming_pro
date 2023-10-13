#! /usr/bin/env python3 

import numpy as np 
import time 

data_points = 4000000
rows = 50
columns = int(data_points / rows)
matrix = np.arange(data_points).reshape(rows, columns)

start = time.time()

res = np.mean(matrix, axis=1)

end = time.time()
print(end - start)