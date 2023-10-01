#! /usr/bin/env python3 

from urllib import parse, robotparser

AGENT_NAME = 'PyMOTW'
URL_BASE = 'https://pymotw.com/'

parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()

PATHS = [
    '/', 
    '/PyMOTW/',
    '/admin/', 
    '/downloads/PyMOTW-1.92.tar.gz',
]

for path in PATHS:
    print(f'{parser.can_fetch(AGENT_NAME, path)!r:>6} -> {path}')
    url = parse.urljoin(URL_BASE, path)
    print(f'{parser.can_fetch(AGENT_NAME, url)!r:>6} -> {url}')
    print()