#! /usr/bin/env python3 

import os 
import json
from src.contacts import Application

class TestLoading:

    def test_load(self):
        app = Application()

        with open('./contacts.json', 'w+') as file:
            json.dump({'_contacts': [('NAME SURNAME', '3333')]}, file)
        
        app.load()

        assert app._contacts == [
            ('NAME SURNAME', '3333',),
        ]


class TestSaving:

    def test_save(self):
        app = Application()
        app._contacts = [('NAME SURNAME', '3333',),]

        try:
            os.unlink('./contacts.json')
        except FileNotFoundError:
            pass

        app.save()

        with open('./contacts.json') as file:
            assert json.load(file) == {'_contacts': [['NAME SURNAME', '3333']]}