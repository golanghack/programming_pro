#! /usr/bin/env python3 

from xml.etree.ElementTree import XMLID

tree, id_map = XMLID(
    """ 
    <root>
        <group>
            <child id="a">This is child "a".</child>
            <child id="b">This is child "b".</child>
        </group>
        <group>
            <child id="c">This is child "c".</child>
        </group>
    </root>
    """
)

for key, value in sorted(id_map.items()):
    print(f'{key} -> {value}')