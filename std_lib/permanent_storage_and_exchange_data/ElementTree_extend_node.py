#! /usr/bin/env python3

from xml.etree.ElementTree import Element, SubElement, tostring, XML
from ElementTree_pretty import prettyfy

top = Element('top')

parent = SubElement(top, 'parent')

children = XML(
    '<root><child num="0"/><child num="1"/>'
    '<child num="2"/></root>'
)

parent.extend(children)

print(prettyfy(top))