#! /usr/bin/env python3 

from src.contacts import App

class TestBasicFeatures:

    def test_international_numbers(self):
        app = App()

        app.run('contacts add NAME +7999999')

        assert app._contacts == [('NAME', '+7999999')]

    def test_invalid_strings(self):
        app = App()
        
        app.run('contacts add NAME InvalidString')

        assert app._contacts == []

class TestStorage:

    def test_reload(self):
        app = App()

        app.run('contacts add NAME 333333')

        assert app._contacts == [('NAME', '333333')]

        app._clear()
        app.load()

        assert app._contacts == [('NAME', '333333')]
        