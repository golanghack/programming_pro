#! /usr/bin/env python3 

"""<--TEXT INDENT-->"""

import re 
import nltk
nltk.download('brown')
from nltk.corpus import brown
import numpy as np

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


probe_text = """The oneperfectly divine thing, the oneglimpse of God’s paradisegiven
on earth, is to fight a losingbattle - and notlose it."""


has_n = [word for word in word_list if 'n' in word]

location_word_in_text = list(set([(m.start(), m.end()) 
                                  for word in word_list 
                                  for m in re.finditer(word, probe_text)]))

start_indent = [m.start() for m in re.finditer(' ', probe_text)]
start_indent.append(-1)
start_indent.append(len(probe_text))
start_indent.sort()

affine_start_indent = [ss + 1 for ss in start_indent]
affine_start_indent.sort()

between_indent = [(start_indent[k] + 1, start_indent[k + 1]) for k in range(0, len(start_indent) - 1)]

not_valid_word = [loc for loc in between_indent if probe_text[loc[0]:loc[1]] not in word_list]

parts_word = [loc for loc in location_word_in_text if loc[0] in affine_start_indent and loc[1] not in start_indent]

lc = not_valid_word[0]


end = [loc2[1] for loc2 in parts_word if loc2[0] == lc[0] and (loc2[1] - lc[0]) > 1]

begin = [loc2[0] for loc2 in end if loc2[1] == lc[1] and (loc2[1] - lc[0] > 1)]

intersection_lists = list(set(end).intersection(begin)
                          )
pivot = np.min(intersection_lists)

text_new = probe_text
text_new = text_new.replace(probe_text[lc[0]:lc[1]], probe_text[lc[0]:pivot] + '' + probe_text[pivot:lc[1]])




