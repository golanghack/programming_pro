#! /usr/bin/env python3

from math import pi 

# calculate period in s from radius in km (Kepler`s third low)
# period = 2pi(gravital_const * mass) ** (-1/2) * radius **(3/2)

gravital_const = 6.674e-11
mass = 1.989e30
radius = 1.496e+09

period: float = (2 * pi) * (gravital_const * mass) ** (-0.5) * (1e3 * radius) ** (3/2)

print(f'new orbital period -> {period/3.156e7:.1f}')

velocity_planet = (2 * pi) * radius / period
print(f'ne orbital period for planet -> {velocity_planet:.2f} km/s') 