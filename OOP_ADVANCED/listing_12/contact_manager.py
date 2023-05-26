#! /usr/bin/env python3 

import pickle
from typing import Dict
from Contact import Contact as contact 

LOOK_UP = 1
ADD = 2
CHANGE = 3 
DELETE = 4
QUIT = 5 
FILENAME = 'contacts.txt'


def load_contacts() -> Dict[str, str]:
    try:
        input_file = open(FILENAME, 'rb')
        dict_contact = pickle.load(input_file)
        input_file.close()
    except EOFError as err:
        print(f'Err -> {err}')
        dict_contact = {}
    return dict_contact

def get_menu_choice() -> int:
    print()
    print('<---MENU--->')
    print('<<<<<<<<<>>>>>>>>>>')
    print('1 -> find contact')
    print('2 -> Add contanct')
    print('3 -> Change contanct')
    print('4 -> Delete contact')
    print('5 -> Exit')
    print()

    choice = int(input('Enter number -> '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter choising mark -> '))
    return choice

def look_up(my_contacts: Dict[str, str]) -> None:
    name = input('Enter name -> ')

    print(my_contacts.get(name, 'Name not found'))

def add(my_contacts: Dict[str, str]) -> None:
    name = input('Name -> ')
    phone = input('Phone -> ')
    email = input('Email -> ')

    entry = contact(name, phone, email)
    if name not in my_contacts:
        my_contacts[name] = entry
        print('Note successfully added')
    else:
        print('This name is already exits')

def change(my_contacts: Dict[str, str]) -> None:
    name = input('Enter name -> ')
    if name in my_contacts:
        phone = input('Enter new phone -> ')
        email = input('Enter new email -> ')

        entry = contact(name, phone, email)

        my_contacts[name] = entry
        print('Note successfully added')
    else:
        print('This name not found')

def delete(my_contacts: Dict[str, str]) -> None:
    name = input('Enter name -> ')
    
    if name in my_contacts:
        del my_contacts[name]
        print('Note delete')
    else:
        print('This name not found')


def save_contacts(my_contacts: Dict[str, str]) -> None:
    output_file = open(FILENAME, 'rb')

    pickle.dump(my_contacts, output_file)
    output_file.close()

def main():
    my_contacts = load_contacts()

    choice = 0 
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(my_contacts)
        elif choice == ADD:
            add(my_contacts)
        elif choice == DELETE:
            delete(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)

    save_contacts(my_contacts)