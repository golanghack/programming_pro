#! /usr/bin/env python3 

from math import pi, sqrt
from astropy.constants import M_sun 
from scipy.constants import G, au, year

radius: float = 10 * au 

print('1 au -> ', au, 'm')
print('1 year -> ', year, 's')
print(f'\nradial distance from Sun -> {radius/au:.1f} au')

# KEpler low
period: float = (2 * pi) * sqrt(radius ** 3 / (G * M_sun.value))
velocity = (2 * pi) * radius / period # m/s

print(f'orbital period -> {period/year:.4f}')
print(f'orbital velocity -> {1e-3 * velocity:.2f} km/s')
