#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CAR REGISTRATION -- ILLUSTRATED BUILDING SERVER WITH TCP PROTOCOL-->"""

import contextlib
import copy
import gzip
import os
import pickle
import random
import socketserver
import struct
import sys 
import threading

class Car:
    """Car class -> formation structure car and methods with work car date"""
    
    def __init__(self, seats: int, mileage: float, owner: str) -> None:
        self.__seats = seats
        self.mileage = mileage
        self.owner = owner
        
    @property
    def seats(self) -> int:
        """count seats in car"""
        
        return self.__seats
    
    @property
    def mileage(self) -> float:
        """count mileage"""
        
        return self.__mileage
    
    @mileage.setter
    def mileage(self, mileage: float) -> float:
        """set miles """
        
        self.__mileage = mileage
        
    @property
    def owner(self) -> str:
        """ return owner"""
        
        return self.__owner
    
    @owner.setter
    def owner(self, owner: str) -> str:
        """Set owner"""
        
        self.__owner = owner
        
class Finish(Exception): pass

class RequestHandler(socketserver.StreamRequestHandler):
    """Building methods for work server"""
    
    cars_lock = threading.Lock()
    call_lock = threading.Lock()
    
    #menu for server functions
    call = dict(
        GET_CAR_DETAILS=(lambda self, *args: self.get_car_details(*args)),
        CHANGE_MILEAGE=(lambda self, *args: self.change_mileage(*args)),
        CHANGE_OWNER=(lambda self, *args: self.change_owner(*args)),
        NEW_REGISTRATION=(lambda self, *args: self.new_registration(*args)),
        SHUTDOWN=(lambda self, *args: self.shutdown(*args))
    ) 
    
    def handle(self) -> None:
        """Formation Struct"""
        size_struct = struct.Struct('!I')
        size_data = self.rfile.read(size_struct.size)
        size = size_struct.unpack(size_data)[0]
        data = pickle.loads(self.rfile.read(size))
        
        try:
            with RequestHandler.call_lock:
                function = self.call[data[0]]
            reply = function(self, *data[1:])
        except Finish:
            return
        data = pickle.dumps(reply, 3)
        self.wfile.write(size_struct.pack(len(data)))
        self.wfile.write(data)
        
    def get_car_details(self, _license):
        """Get car details"""
        
        with RequestHandler.cars_lock:
            car = copy.copy(self.Cars.get(_license, None))
        if car is not None:
            return (True, car.seats, car.mileage, car.owner)
        return (False, 'This license is not registered')
    
    def change_mileage(self, _license: str, mileage: float) -> tuple:
        """Changed mileage for car wit license"""
        
        if mileage < 0:
            return (False, 'Cannot set a negative mileage')
        with RequestHandler.cars_lock:
            car = self.Cars.get(_license, None)
            if car is not None:
                if car.mileage < mileage:
                    car.mileage = mileage
                    return (True, None)
                return (False, 'Cannot wind the odometer back')
        return (False, 'This is not registered')
    
    def change_owner(self, _license: str, owner: str) -> tuple:
        """Changed owner"""
        
        if not owner:
            return (False, 'Cannot set an empty owner')
        with RequestHandler.cars_lock:
            car = self.Cars.get(_license, None)
            if car is not None:
                car.owner = owner
                return (True, None)
        return (False, 'This license is not registered')
    
    def new_registration(self, _license: str, seats: int, mileage: float, owner: str) -> tuple:
        """Registration new car"""
        
        if not _license:
            return (False, 'Cannot set an empty licxense')
        if seats not in {2, 4, 5, 6, 7, 8, 9}:
            return (False, 'Cannot register car with invalid seats')
        if mileage < 0:
            return (False, 'Cannot set a negative mileage')
        if not owner:
            return (False, 'Cannot set an empty owner')
        with RequestHandler.cars_lock:
            if _license not in self.Cars:
                self.Cars[_license] = Car(seats, mileage, owner)
                return (True, None)
        return (False, 'Cannot register duplicate license')
    
    def shutdown(self, *ignore) -> None:
        """Shutdown server"""
        
        self.server.shutdown()
        raise Finish
    
    
class CarRegistrationServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

def save(filename: str, cars: list) -> None:
    """Save"""
    
    try:
        with contextlib.closing(gzip.open(filename, 'wb')) as fh:
            pickle.dump(cars, fh, 3)
    except (EnvironmentError, pickle.UnpicklingError) as err:
        print(f'server failed to save data -> {err}')
        sys.exit(1)
        
def load(filename: str) -> tuple:
    """loading cars informations"""
    
    if not os.path.exists(filename):
        #fake data generate
        cars = {}
        owners = []
        
        for forename, surname in zip(("Warisha", "Elysha", "Liona",
                "Kassandra", "Simone", "Halima", "Liona", "Zack",
                "Josiah", "Sam", "Braedon", "Eleni"),
                ("Chandler", "Drennan", "Stead", "Doole", "Reneau",
                 "Dent", "Sheckles", "Dent", "Reddihough", "Dodwell",
                 "Conner", "Abson")):
            owners.append(forename + " " + surname)
            
        for _license in ("1H1890C", "FHV449", "ABK3035", "215 MZN",
                "6DQX521", "174-WWA", "999991", "DA 4020", "303 LNM",
                "BEQ 0549", "1A US923", "A37 4791", "393 TUT", "458 ARW",
                "024 HYR", "SKM 648", "1253 QA", "4EB S80", "BYC 6654",
                "SRK-423", "3DB 09J", "3C-5772F", "PYJ 996", "768-VHN",
                "262 2636", "WYZ-94L", "326-PKF", "EJB-3105", "XXN-5911",
                "HVP 283", "EKW 6345", "069 DSM", "GZB-6052", "HGD-498",
                "833-132", "1XG 831", "831-THB", "HMR-299", "A04 4HE",
                "ERG 827", "XVT-2416", "306-XXL", "530-NBE", "2-4JHJ"):
            mileage = random.randint(0, 100000)
            seats = random.choice((2, 4, 5, 6, 7))
            owner = random.choice(owners)
            cars[_license] = Car(seats, mileage, owner)
        return cars 
    try:
        with contextlib.closing(gzip.open(filename, 'rb')) as fh:
            return pickle.load(fh)
    except (EnvironmentError, pickle.UnpicklingError) as err:
        print(f'server cannot load data -> {err}')
        sys.exit(1)
        
def main():
    filename = os.path.join(os.path.dirname(__file__), 'car_registration.dat')
    cars = load(filename)
    print(f'Loaded {len(cars)} car registrations')
    
    RequestHandler.Cars = cars
    server = None
    
    try:
        server = CarRegistrationServer(('', 9653), RequestHandler)
        server.serve_forever()
    except Exception as err:
        print('ERROR', err)
    finally:
        if server is not None:
            server.shutdown()
            save(filename, cars)
            print(f'Saved {len(cars)} car registrations')
            
if __name__ == '__main__':
    main()
    
    