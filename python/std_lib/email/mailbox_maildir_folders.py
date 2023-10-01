#! /usr/bin/env python3 

import mailbox
import os 

def show_maildir(name: str) -> None:
    os.system(f'find {name} - print')

mbox = mailbox.Maildir('Example')
print(f'Before -> {mbox.list_folders()}')
show_maildir('Example')

print(f'\n{"":#^30}')

mbox.add_folder('subfolder')
print(f'dubfolder created -> {mbox.list_folders()}')
show_maildir('Example')

subfolder = mbox.get_folder('subfolder')
print(f'subfolder contents -> {subfolder.list_folders()}')

print(f'\n{"":#^30}\n')
subfolder.add_folder('second_level')
print(f'second_level created -> {subfolder.list_folders()}')
show_maildir('Example')

print(f'\n{"":#^30}')
subfolder.remove_folder('second_level')
print(f'second_level removed -> {subfolder.list_folders()}')
show_maildir('Example')