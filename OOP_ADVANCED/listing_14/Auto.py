#! /usr/bin/env python3 

class Auto:

    def __init__(self, 
                    doors: int, 
                    volume: float, 
                    seets: int, 
                    speed: float, 
                    mark: str, 
                    year: int, 
                    country: str, 
                    owner: str, 
                    cost: float, 
                    different: float):
        self.doors = doors
        self.volume = volume
        self.seets = seets
        self.speed = speed
        self.mark = mark
        self.year = year
        self.country = country
        self.owner = owner
        self.cost = cost
        self.different = different

    def set_doors(self, doors):
        self.doors = doors
    def set_volume(self, volume):
        self.volume
    def set_seets(self, seets):
        self.seets
    def set_speed(self, speed):
        self.speed
    def set_mark(self, mark):
        self.mark
    def set_year(self, year):
        self.year
    def set_country(self, country):
        self.country
    def set_owner(self, owner):
        self.owner
    def set_cost(self, cost):
        self.cost
    def set_different(self, different):
        self.different


    def get_doors(self):
        return self.doors
    def get_volume(self):
        return self.volume
    def get_seets(self):
        return self.seets
    def get_speed(self):
        return self.speed
    def get_mark(self):
        return self.mark
    def get_year(self):
        return self.year
    def get_country(self):
        return self.country
    def get_owner(self):
        return self.owner
    def get_cost(self):
        return self.cost
    def get_different(self):
        return self.different

    def distance(self, volume, different_on_hungred_miles):
        """Return different liters on miles"""

        return volume // different_on_hungred_miles



    