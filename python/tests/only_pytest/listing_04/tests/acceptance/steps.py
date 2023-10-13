#! /usr/bin/env python3 

from pytest_bdd import scenario, given, when, then, parsers
from src import contacts

@given('I have a contact book', target_fixture='contactbook')
def contactbook():
    return contacts.App()

@given(parsers.parse('I have a \"{contactname}\" contact'))
def have_a_contaxct(contactbook, contactname):
    contactbook.add(contactname, '000')

@when(parsers.parse('I run the \"{command}\" command'))
def runcommand(contactbook, command):
    contactbook.run(command)