#! /usr/bin/env python3 

from random import randrange

class Monster():

    def __init__(self, rows, cols, speed):
        self.rows = rows, 
        self.cols = cols
        self.my_rows = randrange(self.rows)
        self.my_cols = randrange(self.cols)
        self.my_speed_x = randrange(-speed, speed + 1)
        self.my_speed_y = randrange(-speed, speed + 1)

    def move(self):
        self.my_rows = (self.my_rows + self.my_speed_y) % self.rows
        self.my_cols = (self.my_cols + self.my_speed_x) % self.cols