#! /usr/bin/env python3 

from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettyfy

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This is containts text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This is child has text'
child_with_tail.tail = 'And Tail & that'
print(prettyfy(top))

