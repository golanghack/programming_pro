#! /usr/bin/env python3 

class FiguresCollection:
    """FiguresCollection -> class illustrated duck typing in python."""
    
    def __init__(self) -> None:
        self._triangles = []
        self._squares = []
        self._circles = []
        
    def add(self, figures) -> None:
        if figures.sides() == 3:
            self._triangles.append(figures)
        if figures.sides() == 4:
            self._squares.append(figures)
        if figures.sides() == 0:
            self._circles.append(figures)
            
        