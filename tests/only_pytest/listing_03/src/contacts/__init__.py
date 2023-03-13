#! /usr/bin/env python3 

import re 
import json

class Application:
    
    PHONE_EXPR = re.compile('^[+]?[0-9]{3,}$')

    def __init__(self):
        self._clear()

    def _clear(self) -> None:
        self._contacts = []

    def run(self, text: str):
        text = text.strip()
        _, cmd = text.split(maxsplit=1)

        try:
            cmd, args = cmd.split(maxsplit=1)
        except ValueError:
            args = None
        
        if cmd == 'add':
            name, num = args.rsplit(maxsplit=1)
            try:
                self.add(name, num)
            except ValueError as err:
                print(err)
                return
        elif cmd == 'del':
            self.delete(args)
        elif cmd == 'ls':
            self.print_list()
        else:
            raise ValueError(f'INVALID COMMAND -> {cmd}')

    def save(self):
        with open('./contacts.json', 'w+', encoding='utf-8') as file:
            json.dump({'_contacts': self._contacts}, file)

    
    def load(self):
        with open('./contacts.json', encoding='utf-8') as file:
            self._contacts = [
                tuple(t) for t in json.load(file)['_contacts']
            ]

    def add(self, name: str, phone_number: str):
        if not isinstance(phone_number, str):
            raise ValueError('A valid phone number is required')
        if not self.PHONE_EXPR.match(phone_number):
            raise ValueError(f'INVALID PHONE NUMBER -> {phone_number}')

        self._contacts.append((name, phone_number))
        self.save()

    def delete(self, name: str):
        self._contacts = [
            contact for contact in self._contacts if contact[0] != name
        ]
        self.save()

    def print_list(self):
        for contact in self._contacts:
            print(f'{contact[0]} {contact[1]}')


def main():
    raise NotImplementedError()
    