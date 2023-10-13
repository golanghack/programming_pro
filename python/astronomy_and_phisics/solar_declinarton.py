#! /usr/bin/env python3 

import math 

# day of 1st solstice'
N = 171 
ONE_YEAR = 365.24
ECLIPTIC_ANGULAR = 23.44

# angular velocity in rad/day 
omega = (2 * math.pi) / ONE_YEAR 

# obliquity of the ecliptic
ecliptic = math.radians(ECLIPTIC_ANGULAR) 

# approximate expression for declination of the Sun 
delta = -math.asin(math.sin(ecliptic) * math.cos(omega * (N + 10)))

print(f'declination -> {math.degrees(delta):.2f}')