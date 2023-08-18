#! /usr/bin/env python3 

from xml.etree.ElementTree import XML

def show_node(node: str) -> None:
    print(node.tag)
    if node.text is not None and node.text.strip():
        print(f'text -> {node.text}')
    if node.tail is not None and node.tail.strip():
        print(f'tail -> {node.tail}')
    
    for name, value in sorted(node.attrib.items()):
        print(f'{name} = {value}')
    for child in node:
        show_node(child)
        
parsed = XML(""" 
             <root>
                <group>
                    <child id='a'>This is child 'a'.</child>
                    <child id='b'>This is child 'b'.</child>
                </group>
                <group>
                    <child id='c'>This is child 'c'.</child>
                </group>
            </root>
            """)

print('parsed -> ', parsed)
for elem in parsed:
    show_node(elem)