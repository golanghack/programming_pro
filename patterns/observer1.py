#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--OBSERVER-->"""

import datetime
import itertools
import sys 
import time

def main():
    history_view = HistoryView()
    live_view = LiveView()
    
    model = SliderModel(0, 0, 40)
    model.observers_add(history_view, live_view)
    
    for value in(7, 23, 37):
        model.value = value
    for value, timestamp in history_view.data:
        print(f'{value:3} {datetime.datetime.fromtimestamp(timestamp)}', file=sys.stderr)
        
class Observer:
    """Observer class -> observation """
    
    def __init__(self):
        self.__observers = set()
        
    def observers_add(self, observer: str, *observers: list):
        """Added observer date"""
        
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)
            
    def observer_discard(self, observer: str):
        self.__observers.discard(observer)
        
    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)
            
class SliderModel(Observer):
    
    def __init__(self, minimum: float, value: float, maximum: float) -> None:
        super().__init__()
        #Thrse musst exists before using their property setters
        self.__minimum = self.__value = self.__maximum = None
        self.minimum = minimum
        self.maximum = maximum
        self.value = value
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            self.observers_notify()
    
    @property
    def minimum(self):
        return self.__minimum
    
    @minimum.setter
    def minimum(self, value):
        if self.__minimum != value:
            self.__minimum = value
            self.observers_notify()
            
    @property
    def maximum(self):
        return self.__maximum
    
    @maximum.setter
    def maximum(self, value):
        if self.__maximum != value:
            self.__maximum = value
            self.observers_notify()
            
            
class HistoryView:
    
    def __init__(self):
        self.data = []
        
    def update(self, model):
        self.data.append((model.value, time.time()))
        

class LiveView:
    
    def __init__(self, lenght=40):
        self.lenght = lenght
        
    def update(self, model):
        tipping_point = round(model.value * self.lenght / (model.maximum - model.minimum))
        td = '<td style="background-color: {}">&nbsp;</td'
        html = ['<table style="forn-family: monospace" border="0"><tr>']
        html.extend(td.format('darkblue') * tipping_point)
        html.extend(td.format('cyan') * (self.lenght - tipping_point))
        html.append(f'<td>{model.value}</td></tr></table>')
        print(''.join(html))
        
    
if __name__ == '__main__':
    main()
        