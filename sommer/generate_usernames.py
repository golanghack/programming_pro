#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GENERATE USERNAMES-->"""

import collections
import sys 

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple('User', 'username forename middlename surname id')

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage --> {sys.argv[0]} file1 [file2 [... fileN]]')
        sys.exit()
        
    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding='utf8') as file:
            for line in file:
                line = line.rsprip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)
    
def process_line(line, usernames):
    fields = line.split(':')
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], 
                fields[SURNAME], fields[ID])
    return user

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + 
                 fields[SURNAME]).replace('-', '').replace("'", ''))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = f'{original_name}{count}'
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 32
    usernamewidth = 9
    
    print('{0:<{nw}} {1:^6} {2:{uw}}'.format(
        'Name', 'ID', 'username', nw=namewidth, uw=usernamewidth
    ))
    print('{0:-<{nw}} {0:-<6} {0:-<{uw}}'.format(
        '', nw=namewidth, uw=usernamewidth
    ))
    
    for key in sorted(users):
        user = users[key]
        initial = ''
        if user.middlename:
            initial = ' ' + user.middlename[0]
        name = f'{user.surname}, {user.forename}{initial}'
        print(f'{name:.namewidth} ({user.id:4}) {user.username:usernamewidth}')
        
main()


