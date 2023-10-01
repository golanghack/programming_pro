#! /usr/bin/env python3 

from xml.etree.ElementTree import Element, SubElement, tostring, XML 
from ElementTree_pretty import prettyfy

top = Element('top')

parent_a = SubElement(top, 'parent', id='A')
parent_b = SubElement(top, 'parent', id='B')

# create children nodes 
children = XML(
    '<root><child num="0"/><child num="1"/>'
    '<child num="2"/></root>'
)

# set attributes id with id objects nodes
# for show duplicates
for child in children:
    child.set('id', str(id(child)))
    
# add node in first parent`s node
parent_a.extend(children)

print('A -> ')
print(prettyfy(top))
print()

# copy nodes in second parent`s node
parent_b.extend(children)

print('B -> ')
print(prettyfy(top))
print()