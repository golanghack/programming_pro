#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--DVDS DBM-->

Illustrated method new variated for code exec if -> on dict {}
"""

import datetime
import os 
import pickle
import shelve
import tempfile
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.saxutils
import Console
import Util


DISPLAY_LIMIT = 20

def main():
    functions = dict(a=add_dvd,
                     e=edit_dvd, 
                     l=list_dvds, 
                     r=remove_dvd, 
                     i=import_,
                     x=export,
                     q=quit_)
    filename = os.path.join(os.path.dirname(__file__), 'dvds.dbm')
    db = None
    try:
        db = shelve.open(filename, protocol=pickle.HIGHEST_PROTOCOL)
        action = ''
        while True:
            print(f'\nDVDs ({os.path.basename(filename)}')
            if action != 'l' and 1 <= len(db) <= DISPLAY_LIMIT:
                list_dvds(db)
            else:
                print(f'{len(db)} dvd{Util.s(len(db))}')
            print()
            menu = ('(A)dd (E)dit (L)ist (R)emove (I)mport e(X)port (Q)uit' if len(db) else '(A)dd (I)mport (Q)uit')
            valid = frozenset('aelrixq' if len(db) else 'aiq')
            action = Console.get_menu_choice(menu, valid, 'l' if len(db) else 'a', True)
            functions[action](db)
    finally:
        if db is not None:
            db.close()

def add_dvd(db) -> None:
    """Added object dvd in database"""
    
    title: str = Console.get_string('Title', 'title')
    if not title:
        return
    director: str = Console.get_string('Director', 'director')
    if not director:
        return 
    year: int = Console.get_integer('Year', 'year', minimum=1896, maximum=datetime.date.today().year)
    duration: int = Console.get_integer('Duration (minutes)', 'minutes', minimum=0, maximum=60*48)
    db[title] = (director, year, duration)
    db.sync()
    
    
def edit_dvd(db) -> None:
    """Editor for dvd note in database"""
    
    old_title: str = find_dvd(db, 'edit')
    if old_title is None:
        return
    title = Console.get_string('Title', 'title', old_title)
    if not title:
        return
    director, year, duration = db[old_title]
    director = Console.get_string('Director','director', director)
    if not director:
        return
    year = Console.get_integer('Year', 'year', year, 1896, datetime.date.today().year)
    duration = Console.get_integer('Duration (minutes)', 'minutes', duration, minimum=0, maximum=60*48)
    db[title] = (director, year, duration)
    if title != old_title:
        del db[old_title]
    db.sync()
    
def list_dvds(db) -> None:
    """Formation list of notes dvds in db"""
    
    start = ''
    if len(db) > DISPLAY_LIMIT:
        start = Console.get_string('List those starting with ' '[Enter=all]', 'start')
        print()
        for title in sorted(db, key=str.lower):
            if not start or title.lower().startswith(start.lower()):
                director, year, duration = db[title]
                print('{title} ({year}) {duration} minute{0}, by "{director}"'.format(
                                                                Util.s(duration), **locals()))
                
def remove_dvd(db) -> None:
    """Remove note about dvd in db"""
    
    title = find_dvd(db, 'remove')
    if title is None:
        return
    answer = Console.get_bool(f'Remove {title}?', 'no')
    if answer:
        del db[title]
        db.sync()
        
        
def import_(db) -> None:
    """Import from db in file"""
    
    filename = Console.get_string('Import from', 'filename')
    if not filename:
        return
    try:
        tree = xml.etree.ElementTree.parse(filename)
    except (EnvironmentError, xml.parsers.expat.ExpatError) as err:
        print(f'!!!ERROR!!! -> {err}')
        return
    db.clear()
    for element in tree.findall('dvd'):
        try:
            year = int(element.get('year'))
            duration = int(element.get('duration'))
            director = element.get('director')
            title = element.text.strip()
            db[title] = (director, year, duration)
        except ValueError as err:
            print(f'!!!ERROR!!! -> {err}')
            return
    print(f'Imported {len(db)} dvd{Util.s(len(db))}')
    db.sync()
    
    
def export(db) -> None:
    """Export notes about dvd"""
    
    filename = os.path.join(tempfile.gettempdir(), 'dvds.xml')
    with open(filename, 'w', encoding='utf8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-*"?>\n')
        fh.write('<dvds>\n')
        for title in sorted(db, key=str.lower):
            director, year, duration = db[title]
            fh.write('<dvd year="{year}" duration="{duration}" ' 'director={0}>'.format(
                xml.sax.saxutils.quoteattr(director), **locals()))
            fh.write(xml.sax.saxutils.escape(title))
            fh.write('</dvd>')
        fh.write('</dvds>\n')
        fh.close()
    print(f'exported {len(db)} dvd{Util.s(len(db))} to {filename}')
    
def quit_(db):
    """Exit from db"""
    
    print(f'saved {len(db)} dvd{Util.s(len(db))}')
    db.close()
    
def find_dvd(db, message):
    """Finding dvd"""
    
    message = '(start of) title to ' + message
    while True:
        matches = []
        start = Console.get_string(message, 'title')
        if not start:
            return None
        for title in db:
            if title.lower().startswith(start.lower()):
                matches.append(title)
        if len(matches) == 0:
            print('there are no dvds starting with', start)
            continue
        if len(matches) == 1:
            return matches[0]
        if len(matches) > DISPLAY_LIMIT:
            print(f'Too many dbvds start with {start}; try entering  more of the titlke')
            continue
        else:
            matches = sorted(matches, key=str.lower)
            for i, match in enumerate(matches):
                print(f'{i + 1}: {match}')
            wich = Console.get_integer('Number (or 0 to cancel)', 'number', minimum=1, maximum=len(matches))
            return matches[wich - 1] if wich != 0 else None


if __name__ == '__main__':
    main()    
                
