#! /usr/bin/env python3 

import csv
from xml.etree.ElementTree import iterparse
import sys 

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

qroup_name = ''
parsing = iterparse('podcasts.opml', events=['start'])

for (event, node) in parsing:
    if node.tag != 'outline':
        # ignore all bihind outline
        continue
    if not node.attrib.get('xmlUrl'):
        # save
        group_name = node.attrib['text']
    else:
        # output record
        writer.writerow(
            (group_name, node.attrib['text'], 
             node.attrib['xmlUrl'], 
             node.attrib.get('htmlUrl', ''))
        )