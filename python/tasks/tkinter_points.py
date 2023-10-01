#! /usr/bin/env python3 

from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

def create_grid(event=None):
    w = 800 # Get current width of canvas
    h = 480 # Get current height of canvas
    can1.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 30):
        can1.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 30):
        can1.create_line([(0, i), (w, i)], tag='grid_line')

def fill_grid_square(x, y):
    x1 = x // 30 * 30
    y1 = y // 30 * 30
    x2 = x1 + 30
    y2 = y1 + 30
    can1.create_rectangle(x1, y1, x2, y2)

def karta():
    fi1=0
    item1=can1.create_oval([xstart,ystart],[xstart,ystart],fill="red",outline="red",width=6)
    for i in range (0,6):
        fi1=deltafi+fi1
        x1=math.sin(fi1)*distance[i]
        y1=math.cos(fi1)*distance[i]
        tochka=can1.create_oval([xstart+x1,ystart-y1],[xstart+x1,ystart-y1],fill="black",outline="black",width=4)
        fill_grid_square(xstart+x1, ystart-y1)
        print("x1 ",x1)
        print("y1 ",y1)

    fi2=1.57
    for n in range (6,12):
        fi2=deltafi+fi2
        x2=math.sin(fi2)*distance[n]
        y2=math.cos(fi2)*distance[n]
        tochka=can1.create_oval([xstart+x2,ystart-y2],[xstart+x2,ystart-y2],fill="black",outline="black",width=4)
        fill_grid_square(xstart+x2, ystart-y2)
        print("x2 ",x2)
        print("y2 ",y2)
        print("fi2 ",fi2)

    fi3=3.14
    for p in range(12, 18):
        fi3 = deltafi + fi3
        x3 = math.sin(fi3) * distance[p]
        y3 = math.cos(fi3) * distance[p]
        tochka = can1.create_oval([xstart + x3, ystart - y3], [xstart + x3, ystart - y3], fill="black", outline="black", width=4)
        fill_grid_square(xstart + x3, ystart - y3)
        print("x3 ", x3)
        print("y3 ", y3)

    fi4 = 4.71
    for m in range(18, 24):
        fi4 = deltafi + fi4
        x4 = math.sin(fi4) * distance[m]
        y4 = math.cos(fi4) * distance[m]
        tochka = can1.create_oval([xstart + x4, ystart - y4], [xstart + x4, ystart - y4], fill="black", outline="black", width=4)
        fill_grid_square(xstart + x4, ystart - y4)
        print("x4 ", x4)
        print("y4 ", y4)


okn = tk.Tk()
okn.title('Построение карты')
okn.geometry('800x600')

can1 = Canvas(okn, width=800, height=480, background='white')
can1.place(x=0, y=0)
can1.bind('<Configure>', create_grid)

bt1 = Button(okn, text="START")
bt1.place(x=10, y=500)

bt2 = Button(okn, text="STOP")
bt2.place(x=10, y=540)

deltafi = 0.26  ## 0.26 - это в радианах, 0.26 радианов = 15 градусов
math.degrees(deltafi)
## стартовая точка будет в центре белого прямоугольника: x = 400, y = 240

xstart = 400
ystart = 240

tm0=[73,75,83,102,137,126,121,125,137,100,83,72,72,75,82,97,133,123,118,121,83,79,82,80]
tm1=[95,96,109,133,180,163,155,160,97,68,57,51,49,52,57,68,92,86,82,84,94,90,76,80]
wp=[400,240]
dwp=[-35,-22]

l=1

for l in [1]:
    if l==1:
        distance=tm0
        xstart=xstart+dwp[0]
        ystart=ystart-dwp[1]
        karta()
        l=l+1
    if l==2:
        distance=tm1
        xstart=xstart+dwp[0]
        ystart=ystart-dwp[1]
        karta()
        l=l+1
    


distance.clear()
okn.mainloop()