#! /usr/bin/env python3 

import math 

print('nan, nan -> ', math.isclose(math.nan, math.nan))
print('nan, 1.0 -> ', math.isclose(math.nan, 1.0))
print('inf, inf -> ', math.isclose(math.inf, math.inf))
print('inf, 1.0 -> ', math.isclose(math.inf, 1.0))