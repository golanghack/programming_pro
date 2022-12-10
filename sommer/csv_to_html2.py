#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CSV TO HTML VERSION2 WITH OPTPARSE->"""

import optparse
import sys 
import xml.sax.saxutils


def main():
    parser = optparse.OptionParser()
    parser.add_option('-w', 
                      '--maxwidth', 
                      dest='maxwidth', 
                      type='int', 
                      help=('the maximum number of characters that can be '
                            'output to string fields [default: %default]')
                      )
    parser.add_option('-f',
                      '--format', 
                      dest='format',
                      help=('the format used for outputting numbers '
                            '[default: %default]')
                      )
    parser.set_defaults(maxwidth=100, 
                        format='0.f')
    opts, args = parser.parse_args()
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = 'lightgreen'
            if count % 2:
                color = 'white'
            else:
                color = 'lightyellow'
            print_line(line, color, opts.maxwidth, opts.format)
            count += 1
        except EOFError:
            break
    print_end()
    
def print_start():
    print('<table border="1">')
    
def print_line(line, color, maxwisth, format):
    print(f'<tr bgcolor="{color}"')
    numberFormat = f'<td align="right">{{format: {format}}}</td>'
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print('<td></td>')
        else:
            number = field.replace(',', '')
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(' And ', ' and ')
                if len(field) <= maxwisth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = f'{xml.sax.saxutils.escape(field[:maxwisth])}'
                print(f'<td>{field}</td>')
    print('</tr>')
    

def extract_fields(line):
    fields = []
    field = ''
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            if quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ',':
            fields.append(field)
            field = ''
        else:
            field += c
    if field:
        fields.append(field)
    return fields

def print_end():
    print('<?table>')
    
main()