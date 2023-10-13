#! /usr/bin/env python3 

from Progression import Progression
from ArithmeticProgression import ArithmeticProgression
from GeometricProgression import GeometricProgression
from FibonaccciProgression import FibonacciProgression

print('default progression -> ')
Progression().print_progression(10)

print('An ArithmeticProgression with increment 5 -> ')
ArithmeticProgression(5).print_progression(10)

print('A GeometricProgression wit increment 5 and start 2 -> ')
GeometricProgression(5, 2).print_progression(10)

print('A FibonacciProgression with start values 4 and 6 -> ')
FibonacciProgression(4, 6).print_progression(10)