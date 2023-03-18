#! /usr/bin/env python3 

import re 
import json

class App:

    PHONE_EXPLORER = re.compile('^[+]?[0-9]{3,}$')

    def __init__(self):
        self._clear()

    def _clear(self):
        self._contacts = []

    def run(self, text: str):
        text = text.strip()
        _, command = text.split(maxsplit=1)
        try:
            command, args = command.split(maxsplit=1)
        except ValueError:
            args = None
        
        if command == 'add':
            name, num = args.rsplit(maxsplit=1)
            try:
                self.add(name, num)
            except ValueError as err:
                print(err)
                return 
        elif command == 'del':
            self.delete(args)
        elif command == 'ls':
            self.print_list()
        else:
            raise ValueError(f'Invalid command -> {command}')

    def save(self):
        with open('./contacts.json', 'w+') as file:
            json.dump({'_contacts': self._contacts}, file)

    def load(self):
        with open('./contacts.json') as file:
            self._contacts = [
                tuple(t) for t in json.load(file)['_contacts']
            ]


    def add(self, name, phone_number):
        if not isinstance(phone_number, str):
            raise ValueError('A valid phone number is required')

        if not self.PHONE_EXPLORER.match(phone_number):
            raise ValueError(f'Invalid phone number -> {phone_number}')

        self._contacts.append((name, phone_number))
        self.save()

    def delete(self, name):
        self._contacts = [
            c for c in self._contacts if c[0] != name
        ]
        self.save()

    def print_list(self):
        for c in self._contacts:
            print(f'{c[0]} {c[1]}')

def main():
    import sys 
    a = App()
    a.load()
    a.run(' '.join(sys.argv))