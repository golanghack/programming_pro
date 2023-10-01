#! /usr/bin/env python3 

from xml.etree import ElementTree

with open('data.xml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
node = tree.find('entity_expansion')
print(node.tag)
print('in attribute -> ', node.attrib['attribute'])
print('in text -> ', node.text.strip())
