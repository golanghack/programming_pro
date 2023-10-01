from src import contacts
from pytest_bdd import scenario, given, when, then, parsers

class TestAddingEntries:

    def test_basic(self):
        app = contacts.Application()

        app.run('contacts add NAME 333333333')

        assert app._contacts == [('NAME', '333333333',),]

    def test_surnames(self):
        app = contacts.Application()

        app.run('contacts add AAA 333333')
        app.run('contacts add BBB 222222')
        app.run('contacts add CCC 444444')

        assert app._contacts == [
            ('AAA', '333333'), 
            ('BBB', '222222'), 
            ('CCC', '444444'),
        ]

    def test_internation_numbers(self):
        app  = contacts.Application()

        app.run('contacts add NAME +7333333')

        assert app._contacts == [('NAME', '+7333333',),]

    def test_invalid_strings(self):
        app = contacts.Application()

        app.run('contacts add NAME InvalidString')

        assert app._contacts == []

    def test_reload(self):
        app = contacts.Application()

        app.run('contacts add NAME 333333')

        assert app._contacts == [('NAME', '333333', ),]

        app._clear()
        app.load()

        assert app._contacts == [('NAME', '333333',),]

@scenario('../acceptance/delete_contact.feature', 
            'Removing a Basic Contact')
def test_deleting_contacts():
    pass

@then('My contacts book is now empty')
def empty_list(contactbook):
    assert contactbook._contacts == []

@scenario('../acceptance/list_contacts.feature', 
           'Listing Added Contacts')
def test_listing_added_contacts(capsys):
    pass

@given('I have a first <first> contact')
def have_a_first_contact(contactbook, first):
    contactbook.add(first, '000')
    return first

@given('I have a second <second> contact')
def have_a_second_contact(contactbook, second):
    contactbook.add(second, '000')
    return second

@then('the output contains <listed_contacts> contacts')
def output_contains(listed_contacts, capsys):
    expected_list = ''.join([f'{c} 000\n' for c in listed_contacts.split(',')])
    out, _ = capsys.readouterr()
    assert out == expected_list

@given('I have a contact book', target_fixture='contactbook')
def contactbook():
    return contacts.Application()

@given(parsers.parse('I have a \"{contactname}\" contact'))
def have_a_contact(contactbook, contactname):
    contactbook.add(contactname, '000')

@when(parsers.parse('I run the \"{command}\" command'))
def run_command(contactbook, command):
    contactbook.run(command)