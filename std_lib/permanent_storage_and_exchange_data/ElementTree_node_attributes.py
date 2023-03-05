#! /usr/bin/env python3 

from xml.etree import ElementTree

with open('data.xml', 'rt', encoding='utf-8') as file_:
    tree = ElementTree.parse(file_)
    
node = tree.find('./with_attributes')
print(node.tag)

for name, value in sorted(node.attrib.items()):
    print(f'{name} = {value}')
    
    