#! /usr/bin/env python3 

import imaplib
import re
from imaplib_connect import open_connecttion

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>/*)" (?P<name>.*)')


def parse_list_response(line: str) -> set:
    """return set with flags delimeter and mailbosx_name""" 

    match = list_response_pattern.match(line.decode('utf-8'))
    flags, delimiter, mailbosx_name = match.groups()
    mailbosx_name = mailbosx_name.strip('"')
    return (flags, delimiter, mailbosx_name)

with open_connecttion() as conn:
    typ, data = conn.list()
print('Response code -> ', typ)

for line in data:
    print('Server response -> ', line)
    flags, delimiter, mailbosx_name = parse_list_response(line)
    print('Parsed response -> ', (flags, delimiter, mailbosx_name))