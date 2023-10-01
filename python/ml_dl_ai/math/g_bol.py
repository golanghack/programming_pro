#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
# g=9.8
g = 9.81
# maximum ball
XMAX = 5
# (-v_up/v_down).
cor = 0.65
# interval of animation
dt = 0.005
# start vector and velocity.
x0, y0 = 0, 4
vx0, vy0 = 1, 0
def get_pos(t=0):
    """A generator yielding the ball ' s position at time t."""

    x, y, vx, vy = x0, y0, vx0, vy0
    while x < XMAX:
        t += dt
        x += vx0 * dt
        y += vy * dt
        vy -= g * dt
        if y < 0:
        # Прыжок.
            y = 0
            vy = -vy * cor
        yield x, y

def init():
    """Initialize the animation figure."""

    ax.set_xlim(0, XMAX)
    ax.set_ylim(0, y0)
    ax.set_xlabel('$x$ /m')
    ax.set_ylabel('$y$ /m')
    line.set_data(xdata, ydata)
    ball.set_center((x0, y0))
    height_text.set_text(f'Height: {y0:.1f} m')
    return line, ball, height_text
def animate(pos):
    """For each frame , advance the animation to the new position , pos."""
   
    x, y = pos
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata , ydata)
    ball.set_center((x, y))
    height_text.set_text(f'Height: {y:.1f} m')
    return line, ball, height_text

# new animate for around ball
fig, ax = plt.subplots()
ax.set_aspect('equal')
# supported objects
line, = ax.plot([], [], lw=2)
ball = plt.Circle((x0, y0), 0.08)
height_text = ax.text(XMAX*0.5, y0*0.8, f'Height: {y0:.1f} m')
ax.add_patch(ball)
xdata, ydata = [], []
interval = 1000*dt
ani = animation.FuncAnimation(fig, animate, get_pos, blit=True,
interval=interval, repeat=False, init_func=init)
plt.show()