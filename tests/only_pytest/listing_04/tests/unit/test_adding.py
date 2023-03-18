#! /usr/bin/env python3 

import pytest
from src.contacts import App

class TestAddContacts:

    def test_basic(self):
        app = App()

        app.add('NAME', '323232')
        assert app._contacts == [
            ('NAME', '323232')
        ]

    def test_special(self):
        app = App()

        app.add('Emergency', '911')

        assert app._contacts == [
            ('Emergency', '911')
        ]

    def test_integrational(self):
        app = App()

        app.add('NAME', '+393232323')

        assert app._contacts == [
            ('NAME', '+393232323')
        ]

    def test_invalid(self):
        app = App()

        with pytest.raises(ValueError) as err:
            app.add('NAME', 'not_a_number')

        assert str(err.value) == 'Invalid phone number -> not_a_number'

    def test_short(self):
        app = App()

        with pytest.raises(ValueError) as err:
            app.add('NAME', '19')

        assert str(err.value) == 'Invalid phone number -> 19'

    def test_missing(self):
        app = App()
        
        with pytest.raises(ValueError) as err:
            app.add('NAME', None)

        assert str(err.value) == 'A valid phone number is required'