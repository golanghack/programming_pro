#! /usr/bin/env python3 

""" 
Class Contact 
""" 

class Contact:
    
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_name(self) -> str:
        return self.__name
    
    def get_phone(self) -> str:
        return self.__phone

    def get_email(self) -> str:
        return self.__email

    def __str__(self):
        return f"""Name -> {self.__name}\n, Phone -> {self.__phone}, email -> {self.__email}"""

    