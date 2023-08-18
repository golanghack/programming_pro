#! /usr/bin/env python3 

from xml.etree.ElementTree import (Element, SubElement, Comment, tostring)

top = Element('top')
comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This is child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This is child has text.'
child_with_tail.tail = 'And "Tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print(tostring(top))