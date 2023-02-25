#! /uar/bin/env python3 

from aloe import * 
from nose.tools import assert_equal
from webtest import TestApp
from bank.bank import Bank 
from bank.account import Account 
from bank_app import app

@step(u'account number 0001 is a valid account')
def given_account_number_0001_is_a_valid_account(step):
    account = Account('0001', 50)
    bank = Bank()
    bank.add_account(account)
    
    
@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    
    assert_equal(world.response.status_code, 200)
    assert_equal(world.response.text, u'Hello World')