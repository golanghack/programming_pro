#! /usr/bin/env python3 

from pytest_bdd import scenario, given, when, then, parsers

from src import contacts

from .steps import *


@scenario("features/delete_contact.feature", 
            "Removing a Basic Contact")
def test_deleting_contacts():
    pass


@then("My contacts book is now empty")
def emptylist(contactbook):
    assert contactbook._contacts == []
