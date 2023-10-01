#! /usr/bin/env python3

import imaplib
import configparser
import os 


class AuthSSLException(Exception):
    print('ERROR! Don`t correct password, account or hostname')

# read config
config = configparser.ConfigParser()
config.read([os.path.expanduser('~/.config')])

# connect
hostname = config.get('server', 'hostname')
print('Connecting to -> ', hostname)

connection = imaplib.IMAP4_SSL(hostname)

# auth
username = config.get('account', 'username')
password = 'this_is_the_wrong_password'
print('Logging in as', username)

try:
    connection.login(username, password)
except AuthSSLException as err:
    print(f'ERROR -> {err}')

    


