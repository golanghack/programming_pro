#! /usr/bin/env python3 

"""<--INSERTION INDENT IN TEXT-->"""

import re 
import nltk
nltk.download('brown')
from nltk.corpus import brown
import numpy as np


def insert_indent(text:str, word_list: list) -> str:
    """Insert indent in text"""
    
    location = list(set([(m.start(), m.end()) 
                         for word in word_list 
                         for m in re.finditer(word, text)]))
    start_indent = [m.start() for m in re.finditer(' ', text)]
    start_indent.append(-1)
    start_indent.append(len(text))
    start_indent.sort()
    affine = [aff + 1 for aff in start_indent]
    affine.sort()
    
    parts_word = [loc for loc in location if loc[0] in affine and loc[1] not in  start_indent]
    parts_word_end = [loc for loc in location if loc[0] not in affine and loc[1] in start_indent]
    between_indent = [(start_indent[k] + 1, start_indent[k + 1]) for k in range(0, len(start_indent) -1)]
    notvalid = [loc for loc in between_indent if text[loc[0]:loc[1]] not in word_list]
    
    text_new = text 
    for loc in notvalid:
        end_and_begin = [loc2[1] for loc2 in parts_word if loc2[0] == loc[0]
                         and (loc2[1] - loc[0]) > 1]
        begin_and_end = [loc2[0] for loc2 in parts_word_end if loc2[1] == loc[1]
                         and (loc2[1] - loc[0]) > 1]
        
        pivot = list(set(end_and_begin).intersection(begin_and_end))
    
        if (len(pivot) > 0):
            pivot = np.min(pivot)
            text_new = text_new.replace(text[loc[0]:loc[1]], text[loc[0]:pivot] + ' ' + text[pivot:loc[1]])
    text_new = text_new.replace('  ', ' ')
    return text_new

probe_text = """The oneperfectly divine thing, the oneglimpse of God’s paradisegiven
on earth, is to fight a losingbattle - and notlose it."""


wordlist = set(brown.words())
word_list = list(wordlist)
word_list = [word.replace('*', '') for word in word_list]
word_list = [word.replace('[', '') for word in word_list]
word_list = [word.replace(']', '') for word in word_list]
word_list = [word.replace('?', '') for word in word_list]
word_list = [word.replace('.', '') for word in word_list]
word_list = [word.replace(',', '') for word in word_list]
word_list = [word.replace('+', '') for word in word_list]
word_list = [word.replace('-', '') for word in word_list]
word_list = [word.replace(':', '') for word in word_list]
word_list = [word.replace(';', '') for word in word_list]
word_list = [word.replace(')', '') for word in word_list]
word_list = [word.replace('(', '') for word in word_list]
word_list.remove('')


print(insert_indent(probe_text, word_list))