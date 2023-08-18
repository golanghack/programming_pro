#! /usr/bin/env python3 

""" 
The orbital period of planets in Solar System
"""

import math 
import numpy as np 
import matplotlib.pyplot as plt

from scipy.constants import year, hour, au, G 
from astropy.constants import M_sun 

# in kg
M = M_sun.value

# orbital parameters of planets

# mass in kg
m = 1e24 * np.array([0.33011, 4.8675, 5.9723, 0.64171, 1898.19, 568.34, 86.813, 102.413])

# semi_major axis in m 
a = 1e9 * np.array([57.9, 108.21, 149.60, 227.92, 778.57, 1433.53, 2872.46, 4495.06])

# Kepler`s thirs law to clculate period in sec
T_test_mass = 2 * math.pi * (G * M) ** (-1/2) * a ** (3/2)
T_two_body = 2 * math.pi * (G * (M + m)) ** (-1/2) * a ** (3/2)

print('T [year]  dev  [hour]  dev rel')
for val_1, val_2 in zip(T_test_mass, T_two_body):
    dev = val_1 - val_2
    if dev > hour:
        format_line = '{0:6.2f}  {1:<7.1f}  {2:.1e}'
    else:
        format_line = '{0:6.2f}  {1:7.4f}  {2:.1e}'
    print(format_line.format(val_2/year, dev/hour, dev/val_1)) 

# visualisation with plt
plt.loglog(a / au, T_test_mass / year, 'blue', linestyle='--', label='test mass')
plt.loglog(a / au, T_two_body / year, 'ro', label='planets')
plt.legend(loc='lower right')
plt.xlabel('semy-majot axis [AU]')
plt.ylabel('orbital period [year]')
plt.savefig('third_kepler_low.pdf')
