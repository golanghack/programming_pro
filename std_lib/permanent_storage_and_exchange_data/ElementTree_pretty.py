#! /usr/bin/env python3 

from xml.etree import ElementTree
from xml.dom import minidom

def prettyfy(elem):
    """Return pretty XML string for Element."""
    
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=' ')

