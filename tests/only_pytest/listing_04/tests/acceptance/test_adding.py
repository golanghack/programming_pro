#! /usr/bin/env python3 

from src.contacts import App

class TestAddingEntries:

    def test_basic(self):
        app = App()

        app.run('contacts add NAME 333333')

        assert app._contacts == [('NAME', '333333')]

    def test_surnames(self):
        app = App()

        app.run('contacts add A A 333333')
        app.run('contacts add B B 444444')
        app.run('contacts add C C 555555')

        assert app._contacts == [
            ('A A', '333333'), 
            ('B B', '444444'), 
            ('C C', '555555'),
        ]

        