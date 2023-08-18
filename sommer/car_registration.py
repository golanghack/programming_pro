#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CAR REGISTRATION -- ILLUSTRATED BUILDING CLIENT TCP PROTOCOL-->"""

import collections
import pickle
import socket
import struct
import sys 
import Console

#global list 
Address = ['localhost', 9653]

CarTuple = collections.namedtuple('CarTuple', 'seats mileage owner')

class SocketManager:
    """Manager of contects -> socket"""
    
    def __init__(self, address: tuple) -> None:
        self.address = address
    
    def __enter__(self):
        """Start connection with socket"""
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.address)
        return self.sock
    
    def __exit__(self, *ignore) -> None:
        """Closing socket connection"""
        
        self.sock.close()
        
def main():
    """Formation dict for functions and start menu"""
    
    if len(sys.argv) > 1:
        Address[0] = sys.argv[1]
    #maping function menu  
    call = dict(c=get_car_details, 
                m=change_mileage, 
                o=change_owner, 
                n=new_registration, 
                s=stop_server, q=_quit)
    
    menu = ('(C)ar Edit (M)ileage Edit (O)wner (N)ew car   '
            '(S)top server (Q)uit')
    valid = frozenset('cmonsq')
    previouse_license = None
    
    while True:
        action = Console.get_menu_choice(menu, valid, 'c', True)
        previouse_license = call[action](previouse_license)
        
def retrieve_car_details(previouse_license) -> tuple:
    """Get car details for formation struct"""
    
    _license = Console.get_string('License', 'license', previouse_license)
    
    if not _license:
        return previouse_license, None
    _license = _license.upper()
    ok, *data = handle_request('GET_CAR_DETAILS', _license)
    
    if not ok:
        print(data[0])
        return previouse_license, None
    return _license, CarTuple(*data)


def get_car_details(previouse_license)  -> tuple:
    """Get car details and formations info message"""
    
    _license, car = retrieve_car_details(previouse_license)
    if car is not None:
        print('License --> {0}\nSeats --> {seats}\nMileage --> {mileage}\n'
              'Owner --> {owner}'.format(_license, **car._asdict()))
    return _license

def change_mileage(previouse_license) -> tuple:
    """Set mileage"""
    
    _license, car = retrieve_car_details(previouse_license)
    if car is None:
        return previouse_license
    mileage = Console.get_integer('Mileage', 'mileage', car.mileage, 0)
    if mileage == 0:
        return _license
    ok, *data = handle_request('CHANGE_MILEAGE', _license, mileage)
    
    if not ok:
        print(data[0])
    else:
        print('Mileage successfully changed')
    return _license

def change_owner(previouse_license) -> tuple:
    """set owner"""
    
    _license, car = retrieve_car_details(previouse_license)
    if car is None:
        return previouse_license
    owner = Console.get_string('Owner', 'owner', car.owner)
    if not owner:
        return _license
    ok, *data = handle_request('CHANGE_OWNER', _license, owner)
    
    if not ok:
        print(data[0])
    else:
        print('Owner successfully changed')
    return _license

def new_registration(previouse_license) -> tuple:
    """New registration and fomation info table"""
    
    _license = Console.get_string('License', 'license')
    
    if not _license:
        return previouse_license
    _license = _license.upper()
    seats = Console.get_integer('Seats', 'seats', 4, 0)
    
    if not(1 < seats < 10):
        return previouse_license
    mileage = Console.get_integer('Mileage', 'mileage', 0, 0)
    owner = Console.get_string('Owner', 'owner')
    
    if not owner:
        return previouse_license
    ok, *data = handle_request('NEW_REGISTRATION', _license, seats, mileage, owner)
    
    if not ok:
        print(data[0])
    else:
        print(f'Car {_license} successfully registered')
    return _license

#*ignore -> function ignoring all parameters
def _quit(*ignore) -> None:
    """Quit"""
    
    sys.exit()
#*ignore -> function ignoring all parameters  
def stop_server(*ignore) -> None:
    """Stop server"""
    
    handle_request('SHUTDOWN', wait_for_reply=False)
    sys.exit()
    
def handle_request(*items, wait_for_reply=True):#wait_for_reply -> answer from server
    """Formation socket connection and requesting -> Building Struct"""
    
    #one number 
    size_struct = struct.Struct('!I')
    #protocol conserving -> 3
    data = pickle.dumps(items, 3)
    
    try:
        with SocketManager(tuple(Address)) as sock:
            sock.sendall(size_struct.pack(len(data)))
            sock.sendall(data)
            
            if not wait_for_reply:
                return
            #answer from server
            size_data = sock.recv(size_struct.size)
            size = size_struct.unpack(size_data)[0]
            result = bytearray()
            
            while True:
                data = sock.recv(4000)
                if not data:
                    break
                result.extend(data)
                
                if len(result) >= size:
                    break
                
        return pickle.loads(result)
    except socket.error as err:
        print(f'{err} -> is the server running?')
        sys.exit(1)
        
        
if __name__ == '__main__':
    main()
        
    
        
