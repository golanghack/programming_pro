#!/usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--TAMPLATE-->"""

import abc 
import html.parser
import os 
import re
import sys 

class AbstractWordCounter(metaclass=abc.ABCMeta):
    
    @staticmethod
    @abc.abstractmethod
    def can_count(filename: str) -> str:
        pass
    
    @staticmethod
    @abc.abstractmethod
    def count(filename: str) -> int:
        pass

class PlainTextWordCounter(AbstractWordCounter):
    
    @staticmethod
    def can_count(filename: str) -> str:
        return filename.lower().endswith('.txt')
    
    @staticmethod
    def count(filename: str) -> int:
        if not PlainTextWordCounter.can_count(filename):
            return 0
        regex = re.compile(r'\w+')
        total = 0
        with open(filename, encoding='utf-8') as file:
            for line in file:
                for _ in regex.finditer(line):
                    total += 1
        return total

class HtmlWordCounter(AbstractWordCounter):
    
    class _HamlParser(html.parser.HTMLParser):
        
        def __init__(self):
            super().__init__()
            self.regex = re.compile('\w+')
            self.in_text = True
            self.text = []
            self.count = 0
            
        def handle_starttag(self, tag: str, attrs: list) -> bool:
            if tag in {'script', 'style'}:
                self.in_text = False
                
        def handle_endtag(self, tag: str):
            if tag in {'script', 'style'}:
                self.in_text = True
            else:
                for _ in self.regex.finditer(''.join(self.text)):
                    self.count += 1
                self.text = []
                
        def handle_data(self, text: str) -> list:
            if self.in_text:
                text = text.rstrip()
                if text:
                    self.text.append(text)
    @staticmethod
    def can_count(filename: str) -> str:
        return filename.lower().endswith(('.htm', '.html'))
    
    @staticmethod
    def count(filename: str) -> int:
        if not HtmlWordCounter.can_count(filename):
            return 0
        parser = HtmlWordCounter._HamlParser()
        with open(filename, encoding='utf-8') as file:
            parser.feed(file.read())
        return parser.count
    
def count_words_in_files(files: list) -> str:
    """ciunting word in files. total -> counter"""
    
    total: int = 0
    for filename in files:
        count = count_words(filename)
        if count is not None:
            total += count
            print(f'{count:9,} words in {filename}')
    print(f'total -> {total,} words')
    
def count_words(filename: str) -> int:
    """Used classes AbstractWordCounter, HtmlWordCounter, PlainTextWordCounter"""
    
    for word_counter in (PlainTextWordCounter, HtmlWordCounter):
        if word_counter.can_count(filename):
            return word_counter.count(filename)

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage -> {os.path.basename(sys.argv[0])} <files>')
    count_words_in_files(sys.argv[1:])
    
if __name__ == '__main__':
    main()