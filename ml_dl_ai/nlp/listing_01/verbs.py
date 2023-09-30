#! /usr/bin/env python3 

import spacy as sp 

nlp = sp.load('en_core_web_sm')
doc = nlp('I have flown to Moscow.Now I am flying to Madrid')
print([word.text for word in doc if word.tag_ == 'VBG' or word.tag_ == 'VB'])