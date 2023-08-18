#! /usr/bin/env python3 

class Customer:
    """Customer -> class for idetification owner
    parameters:
    name -> name pf client -> str
    address -> address of client -> str
    phone -> phone number of client -> int
    This class create object for these customisation 
    data of client
    """ 

    def __init__(self, name: str, address: str, phone: int) -> None:
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_address(self, address: str) -> None:
        self.__address = address

    def set_phone(self, phone: int) -> None:
        self.__phone = phone

    def get_name(self) -> str:
        return self.__name

    def get_address(self) -> str:
        return self.__address
    
    def get_phone(self) -> int:
        return self.__phone

    