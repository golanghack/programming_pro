#! /usr/bin/env python3 

import numpy as np 
import matplotlib.pyplot as plt 
from into_functions import Chain
from elementary_function import square
from deriv import deriv
from sigmoid import sigmoid, chain_deriv_2

PLOT_RANGE = np.arange(-3, 3, 0.01)

chain_1 = [square, sigmoid]
chain_2 = [sigmoid, square]

print(chain_1, PLOT_RANGE)
print(chain_1, PLOT_RANGE)
print(chain_2, PLOT_RANGE)
print(chain_2, PLOT_RANGE)
