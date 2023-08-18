#! /usr/bin/env python3 

""" 
The following program computes the tidal force per unit mass, a tidal = F/m,
for a grid of points with equal spacing along the x- and y-axes within a circle of
radius R = Re
"""


import numpy as np 
from scipy.constants import g, G 
from astropy.constants import R_earth, M_earth
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# mass of the Moon in kg
M = 0.07346e24

# radius orbit m 
r = 3.844e8 

coeff = G * M / r ** 3 
accel_scale = 2 * coeff * R_earth.value

print(f'tidal acceleration = {accel_scale:.2e} m/s^2 = {accel_scale/g:2e} g')

# height 
h = 15 * M * R_earth.value ** 4 / (8 * M_earth.value * r ** 3)
print(f'size of todal buldge -> {h:.2f} meters')

# array of evently spaced grid points along x- and y-axis
X = np.linspace(-1.1, 1.1, num=23, endpoint=True)
Y = np.linspace(-1.1, 1.1, num=23, endpoint=True)
print(X)

# create two-dimensional mesh grid scaled by Earth rwdius
R_x, R_y = np.meshgrid(R_earth.value * X, R_earth.value * Y)
print(R_x.shape)
print(R_x[11, 21], R_y[11, 21])

# radial distance of mesh poijnts from (0, 0)
R = np.sqrt(R_x * R_x + R_y * R_y)

# components of tidal accelaratiuon field within Eartsh radius
accel_x = np.ma.masked_where(R > R_earth.value, 2 * coeff * R_x)
accel_y = np.ma.masked_where(R > R_earth.value, -coeff * R_y)


# visualisation
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
# plot vector field
arrows = ax.quiver(X, Y, accel_x, accel_y, color='blue')
ax.quiverkey(arrows, X=0.1, Y=0.95, U=accel_scale,label=r'$1.1\times 10^{-6}\;\mathrm{m/s}^2$', labelpos='E')
# add a circle
circle = Circle((0, 0), 1, alpha=0.2, edgecolor=None)
ax.add_patch(circle)
ax.set_xlabel(r'$x/R_{\mathrm{E}}$', fontsize=12)
ax.set_ylabel(r'$y/R_{\mathrm{E}}$', fontsize=12)
plt.show()
plt.savefig("tidal_accel_earth.pdf")