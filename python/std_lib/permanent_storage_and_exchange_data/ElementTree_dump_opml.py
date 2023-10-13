#! /usr/bin/env python3 

from xml.etree import ElementTree
import pprint

with open('podcasts.opml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
for node in tree.iter():
    pprint.pprint(node.tag)