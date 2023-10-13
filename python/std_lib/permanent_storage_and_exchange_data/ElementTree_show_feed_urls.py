#! /usr/bin/env python3 

from xml.etree import ElementTree

with open('podcasts.opml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    
    if name and url:
        print(f'{  name}')
        print(f'{  url  }')
    else:
        print(name)
    