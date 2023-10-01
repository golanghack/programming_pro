#! /usr/bin/env python3 

import pytest
from src.contacts import Application

class TestAddContacts:

    def test_basic(self):
        app = Application()

        app.add('NAME', '222222')

        assert app._contacts == [('NAME', '222222',),]

    def test_special(self):
        app = Application()

        app.add('Emergency', '911')

        assert app._contacts == [('Emergency', '911',),]

    def test_international(self):
        app = Application()

        app.add('NAME', '+7222222')

        assert app._contacts == [('NAME', '+7222222',),]

    def test_invalid(self):
        app = Application()

        with pytest.raises(ValueError) as err:
            app.add('NAME', 'not_a_number')

        assert str(err.value) == 'INVALID PHONE NUMBER -> not_a_number'

    def test_short(self):
        app = Application()

        with pytest.raises(ValueError) as err:
            app.add('NAME', '19')

        assert str(err.value) == 'INVALID PHONE NUMBER -> 19'

    def test_missing(self):
        app = Application()

        with pytest.raises(ValueError) as err:
            app.add('NAME', None)

        assert str(err.value) == 'A valid phone number is required'