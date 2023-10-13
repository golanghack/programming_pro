#! /usr/bin/env python3 

from xml.etree import ElementTree

with open('data.xml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
for path in ['./child', './child_with_tail']:
    node = tree.find(path)
    
    print(node.tag)
    print('child node text -> ', node.text)
    print('and tail text -> ', node.tail)