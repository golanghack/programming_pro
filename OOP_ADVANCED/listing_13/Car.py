#! /usr/bin/env python3 

class Car:

    def __init__(self, make: str, model: str, year: int) -> None:
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make: str) -> None:
        self.__make = make

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_year(self, year: int) -> None:
        self.__year = year

    def get_make(self) -> str:
        return self.__make

    def get_model(self) -> str:
        return self.__model
        
    def get_year(self) -> int:
        return self.__year

    