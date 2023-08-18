#! /usr/bin/env python3 

from xml.etree.ElementTree import Element, tostring
from ElementTree_pretty import prettyfy

top = Element('top')

children = [
    Element('child', num=str(i)) for i in range(3)
]

top.extend(children)

print(prettyfy(top))