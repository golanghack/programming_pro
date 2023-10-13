#! /usr/bin/env python3 

"""Class Bus 
school bus for road.
to moving and into passengers and out passengers
""" 

class Bus:
    def __init__(self, passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name: str) -> None:
        self.passengers.append(name)
    
    def drop(self, name: str) -> None:
        self.passengers.remove(name)

        