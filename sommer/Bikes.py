#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--BIKES MODULE-->"""


"""
>>> import os
>>> import tempfile
>>> bike_file = os.path.join(tempfile.gettempdir(), "bikes.dat")
>>> if os.path.exists(bike_file): os.remove(bike_file)

>>> bike_data = []
>>> bike_data.append(('REFK2', 'Reflex Kalahari', 5, 200.97))
>>> bike_data.append(('REFT1', 'Reflex Tempus', 4, 200.97))
>>> bike_data.append(('UNISTOW', 'Universal Stowaway', 1, 203.00))
>>> bike_data.append(('REFONA', "Reflex Out 'n' About", 0, 213.15))
>>> bike_data.append(('B4U16RS', 'Bicycles4U 16/6/RS  ', 0, 223.30))
>>> bike_data.append(('B4U20', 'Bicycles4U 20/6', 9, 223.30))
>>> bike_data.append(('B4U20MTB', 'Bicycles4U 20/6/MTB', 5, 223.30))
>>> bike_data.append(('REFA3', 'Reflex Axiom 3', 15, 223.30))
>>> bike_data.append(('ASBC', 'AS Bikes Compact', 22, 243.60))
>>> bike_data.append(('AMMC', 'Ammaco Commuter', 4, 259.84))
>>> bike_data.append(('AMMP5', 'Ammaco Pakka Mk 5', 7, 259.84))
>>> bike_data.append(('B4U20RS', 'Bicycles4U 20/6/RS', 3, 263.90))
>>> bike_data.append(('COM16', 'Compass 16"', 2, 263.90))
>>> bike_data.append(('ASBC+', 'AS Bikes Compact Plus', 11, 284.20))
>>> bike_data.append(('TIGB', 'Tiger Bikes', 0, 284.20))
>>> bike_data.append(('ASBEX', 'AS Bikes Explorer', 2, 304.50))
>>> bike_data.append(('GEKKO', 'Gekko', 6, 304.50))
>>> bike_data.append(('PROBE', 'Probike Enfold', 4, 304.50))
>>> bike_data.append(('SAMHDXM', 'Samchuly Haro DX MTB', 5, 304.50))
>>> bike_data.append(('SINAB', 'Sinclair A-Bike', 3, 304.50))
>>> bike_data.append(('FALOM', 'Falcon Optima Mayfair', 2, 324.80))
>>> bike_data.append(('RALPARK', 'Raleigh Parkway', 1, 324.80))
>>> bike_data.append(('SAXS', 'Saxon Safari', 2, 324.80))
>>> bike_data.append(('CLACHA', 'Classic Chatsworth', 0, 328.86))
>>> bike_data.append(('ASBE+', 'AS Bikes Explorer Plus', 3, 345.10))
>>> bike_data.append(('RALPROM', 'Raleigh Promenade', 2, 345.10))
>>> bike_data.append(('VIKBS', 'Viking Bikes Safari', 1, 345.10))
>>> bike_data.append(('AMMT+C', 'Ammaco Town & Country', 0, 353.22))
>>> bike_data.append(('AMMCT', 'Ammaco Cruiser Tandem 16"', 0, 355.25))
>>> bike_data.append(('AMMMON', 'Ammaco Montreal', 4, 355.25))
>>> bike_data.append(('MSGENIE', 'Mission Space Genie', 4, 355.25))
>>> bike_data.append(('TRANSS', 'Transair Sea Sure', 3, 355.25))
>>> bike_data.append(('DAHSP', 'Dahon Sweet Pea', 1, 363.37))
>>> bike_data.append(('SALEASY', 'Salcano Easy', 0, 365.40))
>>> bike_data.append(('CLAMEL', 'Classic Melbourne', 1, 379.61))
>>> bike_data.append(('VENTGL', 'Ventura Go Lite', 1, 383.67))

>>> bicycles = BikeStock(bike_file)
>>> for bike in bike_data:
...     bicycles.append(Bike(*bike))
>>> bicycles["VIKBS"].name
'Viking Bikes Safari'
>>> ok = []
>>> value = 0.0
>>> for i, bike in enumerate(bicycles):
...     ok.append(bike.quantity == bike_data[i][2])
...     value += bike.value
>>> all(ok), "{0:.2f}".format(round(value, 2))
(True, '35969.57')
>>> bicycles["SALEASY"].name
'Salcano Easy'
>>> bicycles.change_name("SALEASY", "Salcano EZ")
True
>>> bicycles["SALEASY"].name
'Salcano EZ'
>>> total = 0
>>> for bike in bicycles:
...     if bike.identity.startswith("B4U"):
...         total += bike.quantity
>>> total
17
>>> total = 0
>>> for bike in bicycles:
...     if bike.identity.startswith("B4U"):
...         if bicycles.increase_stock(bike.identity, 2):
...             total += bicycles[bike.identity].quantity
...         else:
...             print("error", bike)
>>> total
25
>>> value = 0.0
>>> count = 0
>>> for bike in bicycles:
...     value += bike.value
...     count += 1
>>> "{0:.2f}".format(round(value, 2)), count, count == len(bike_data)
('37837.17', 36, True)
>>> bicycles["CLAMEL"].name
'Classic Melbourne'
>>> del bicycles["UNISTOW"]
>>> value = 0.0
>>> count = 0
>>> for bike in bicycles:
...     value += bike.value
...     count += 1
>>> "{0:.2f}".format(round(value, 2)), count
('37634.17', 35)
>>> bicycles["CLAMEL"].name
'Classic Melbourne'
>>> bicycles.append(Bike('UNISTOW', 'Universal Stowaway', 1, 203.00))
>>> bicycles.close()

>>> bicycles = BikeStock(bike_file)
>>> value = 0.0
>>> for bike in bicycles:
...     value += bike.value
>>> "{0:.2f}".format(round(value, 2))
'37837.17'
>>> bicycles.close()
>>> os.path.getsize(bike_file)
1836
>>> if os.path.exists(bike_file): os.remove(bike_file)
"""

