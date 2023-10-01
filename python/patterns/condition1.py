#!/usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--CONDITION-->"""

import collections
import random

random.seed(917)

def generate_random_events(count: int):
    """Genarator sporadic events"""
    
    vehicles = (('cars', ) * 11) + (('vans', ) * 3) + ('trucks',)
    for _ in range(count):
        yield Event(random.choice(vehicles), random.randint(1, 3))
    
class Counter:
    """Countiong objs"""
    
    def __init__(self,  *names: list) -> None:
        self.anonymous = not bool(names)
        if self.anonymous:
            self.count = 0
        else:
            for name in names:
                if not name.isidentifier():
                    raise ValueError('names mast be valid identifiers')
                setattr(self, name, 0)
                
    def __call__(self, event: str):
        if self.anonymous:
            self.count += event.count
        else:
            count = getattr(self, event.name)
            setattr(self, event.name, count + event.count)
            
            
class Event:
    
    def __init__(self, name: str, count: int=1) -> None:
        if not name.isidentifier():
            raise ValueError('names must be valid identifiers')
        self.name = name
        self.count = count
        
    
class Multiplexer:
    
    ACTIVE, DORMANT = ('ACTIVE', 'DORMANT')
    
    def __init__(self):
        self.callbacks_for_event = collections.defaultdict(list)
        self.state = Multiplexer.ACTIVE
        
    def connect(self, evemt_name: str, callback: str):
        if self.state == Multiplexer.ACTIVE:
            self.callbacks_for_event[evemt_name].append(callback)
            
    def disconnect(self, event_name: str, callback: str=None):
        if self.state == Multiplexer.ACTIVE:
            if callback is None:
                del self.callbacks_for_event[event_name]
            else:
                self.callbacks_for_event[event_name].remove(callback)
                
    def send(self, event: str):
        if self.state == Multiplexer.ACTIVE:
            for callback in self.callbacks_for_event.get(event.name, ()):
              callback(event)

def main():
    total_counter = Counter()
    car_counter = Counter('cars')
    commercial_counter = Counter('vans', 'trucks')
    
    multiplexer = Multiplexer()
    for event_name, callback in (('cars', car_counter), ('vans', commercial_counter), ('trucks', commercial_counter)):
        multiplexer.connect(event_name, callback)
        multiplexer.connect(event_name, total_counter)
    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"""After 1-- active events -> 
          cars -> {car_counter.cars} 
          vans -> {commercial_counter.vans}
          trucks -> {commercial_counter.trucks}
          total -> {total_counter.count}""")
    
    multiplexer.state = Multiplexer.DORMANT
    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"""After 100 dormant events -> 
          cars -> {car_counter.cars} 
          vans -> {commercial_counter.vans} 
          trucks -> {commercial_counter.trucks} 
          total -> {total_counter.count}""")
    
    multiplexer.state = Multiplexer.ACTIVE
    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"""After 100 active events ->  
          cars -> {car_counter.cars} 
          vans -> {commercial_counter.vans} 
          trucks -> {commercial_counter.trucks}
          total -> {total_counter.count}""")
                
if __name__ == '__main__':
    main()