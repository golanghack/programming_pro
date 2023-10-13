#! /usr/bin/env python3 

import numpy as np 
from scipy.optimize import curve_fit


# data
xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

def linear_model(numpy_massive, const_a: float, const_b: float) -> float:
    return const_a * numpy_massive + const_b 


def quadratic_model(numpy_massive, const_a: float, const_b: float):
    return const_a * numpy_massive * numpy_massive + const_b * numpy_massive


(a, b), _ = curve_fit(linear_model, xs, ys)
print(f'Linear regression -> = {a} * N + {b}')

(a, b), _ = curve_fit(quadratic_model, xs, ys)
print(f'Quadratic regression -> {a} * N * N + {b} * N')