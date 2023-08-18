#! /usr/bin/env python3 

from Monster import Monster

MANY_MONSTERS = 20 
ROWS = 100 
COLS = 200 
SPEED = 4 

moster_list = []

for i in range(MANY_MONSTERS):
    new_monster = Monster(ROWS, COLS, SPEED)
    moster_list.append(new_monster)

for j in moster_list:
    new_monster.move()


