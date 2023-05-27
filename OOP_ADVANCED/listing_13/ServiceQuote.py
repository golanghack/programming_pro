#! /usr/bin/env python3 

TAX_RATE = 0.05

class ServiceQuote:

    def __init__(self, middle_working: str, large_working: str) -> None:
        self.__partst_middle_working = middle_working
        self.__parts_large_working = large_working

    def set_parts_middle(self, middle_working: str) -> None:
        self.__partst_middle_working = middle_working

    def set_large_working(self, large_working: str) -> None:
        self.__parts_large_working = large_working

    def get_parts_middle(self) -> str:
        return self.__partst_middle_working
    
    def get_parts_large(self) -> str:
        return self.__parts_large_working

    def get_total(self) -> str:
        return self.__partst_middle_working + self.__parts_large_working + (self.__partst_middle_working * TAX_RATE)