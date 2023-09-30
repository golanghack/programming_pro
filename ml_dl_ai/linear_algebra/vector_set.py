#! /usr/bin/env python3

"""Create vector set"""

import numpy as np 
import matplotlib.pyplot as plt 


# create set with one vector
vector = np.array([1, 3])

# random integers from -4 to +4 to size 100
xlimit = [-4, 4]
scalars = np.random.uniform(low=xlimit[0], high=xlimit[1], size=100)

# dotted
plt.figure(figsize=(6, 6))

for scalar in scalars:
    # point
    point = vector * scalar
    # draw 
    plt.plot(point[0], point[1], 'ko')

plt.xlim(xlimit)
plt.ylim(xlimit)
plt.grid()
plt.text(-4.5, 4.5, 'Vector', fontweight='bold', fontsize=24)
plt.savefig('vector_and_scalar.png', dpi=500)
plt.show()

