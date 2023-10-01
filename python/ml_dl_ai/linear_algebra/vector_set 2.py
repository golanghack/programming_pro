#! /usr/bin/env python3

import plotly.graph_objects as go 
import numpy as np 

# two vectors in r3
vector_one = np.array([3, 13, 32])
vector_two = np.array([0, 43, 22])

xlimit = [-4, 4]

scalars = np.random.uniform(low=xlimit[0], high=xlimit[1], size=(100, 2))

# points
points = np.zeros((100, 3))
for i in range(len(scalars)):
    # combintaions on two vectors
    points[i, :] = vector_one * scalars[i, 0] + vector_two * scalars[i, 1]

# draw 
figure = go.Figure(data=[go.Scatter3d(
    x=points[:, 0], 
    y=points[:, 1],
    z=points[:, 2],
    mode='markers',
    marker=dict(size=6, color='red')
)])
figure.update_layout(margin=dict(l=0, r=0, b=0, t=0))
figure.show()