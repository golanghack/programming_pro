#! /usr/bin/env python3 

import io 
import sys 
from xml.etree.ElementTree import Element, SubElement, ElementTree

top = Element('top')

child = SubElement(top, 'child')
child.text = 'Contains text'

empty_child = SubElement(top, 'empty_child')

for method in ['xml', 'html', 'text']:
    print(method)
    sys.stdout.flush()
    ElementTree(top).write(sys.stdout.buffer, method=method)
    print('\n')