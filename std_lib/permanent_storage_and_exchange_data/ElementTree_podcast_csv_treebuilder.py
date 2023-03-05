#! /usr/bin/env python3 

import csv
import io   
from xml.etree.ElementTree import XMLParser
import sys 

class PodcastListToCSV(object):
    
    def __init__(self, output_file: str) -> None:
        self.writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC,)
        self.group_name = ''
        
    def start(self, tag: str, attrib: str) -> None:
        if tag != 'outline':
            # ignore
            return
        if not attrib.get('xmlUrl'):
            # save
            self.group_name = attrib['text']
        else:
            # output record
            self.writer.writerow(
                (self.group_name,
                 attrib['text'],
                 attrib['xmlUrl'], 
                 attrib.get('htmlUrl', ''))
            )
            
    def end(self, tag: str) -> None:
        'Ignore closing tags'
        
    def data(self, data) -> None:
        'Ignore data inside nodes'
    
    def close(self) -> None:
        'Nothing special to do here'
        
        
target = PodcastListToCSV(sys.stdout)
parser = XMLParser(target=target)

with open('podcasts.opml', 'rt', encoding='utf-8') as file_:
    for line in file_:
        parser.feed(line)
        
parser.close()