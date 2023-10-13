#! /usr/bin/env python3 
from typing import NamedTuple
from dataclasses import dataclass


class Coordinate(NamedTuple):
    latitude: float
    longitude: float

    def __str__(self):
        ns = 'N' if self.latitude >= 0 else 'S'
        we = 'E' if self.longitude >= 0 else 'W'
        return f'{abs(self.latitude):.1f}{ns}, {abs(self.longitude):.1f}{we}'
    
@dataclass(frozen=True)
class CoordinateDC:
    latitude: float
    longitude: float

    def __str__(self):
        ns = 'N' if self.latitude >= 0 else 'S'
        we = 'E' if self.longitude >= 0 else 'W'
        return f'{abs(self.latitude):.1f}{ns}, {abs(self.longitude):.1f}{we}' 