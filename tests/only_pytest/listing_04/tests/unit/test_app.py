#! /usr/bin/env python3 

from unittest import mock
import pytest
from src.contacts import App

def test_app():
    app = App()

    assert app._contacts == []
    assert hasattr(app, 'run')

def test_clear():
    app = App()
    app._contacts = [('NAME', "NUM")]

    app._clear()

    assert app._contacts == []

class TestRun:

    def test_add(self):
        app = App()

        with mock.patch.object(app, 'add') as mocked:
            app.run('command add NAME 333')

        mocked.assert_called_with('NAME', '333')

    def test_add_surname(self):
        app = App()

        with mock.patch.object(app, 'add') as mocked:
            app.run('command add NAME SURNAME   333   ')

        mocked.assert_called_with('NAME SURNAME', '333')

    def test_empty(self):
        app = App()

        with pytest.raises(ValueError):
            app.run('')

    def test_no_commands(self):
        app = App()

        with pytest.raises(ValueError):
            app.run('no command')

    def test_invalid(self):
        app = App()

        with pytest.raises(ValueError):
            app.run('contacts invalid')