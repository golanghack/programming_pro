#! /usr/bin/env python3 

import imaplib
import configparser
import os 

def open_connecttion(verbose: bool=False) -> imaplib.IMAP4_SSL:
    """open connection for ssl"""

    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.config')])

    # connect to server 
    hostname = config.get('server', 'hostname')
    if verbose:
        print('Connectiong to ', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # into auth
    username = config.get('account', 'username')
    password = config.get('account', 'password')

    if verbose:
        print('logging in as', username)
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    with open_connecttion(verbose=True) as conn:
        print(conn)