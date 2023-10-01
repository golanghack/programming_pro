#! /usr/bin/env python3 

from xml.etree import ElementTree

with open('podcasts.opml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print(url)