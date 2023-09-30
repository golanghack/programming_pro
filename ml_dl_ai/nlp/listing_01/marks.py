#! /usr/bin/env python3 

import spacy as sp 

nlp = sp.load('en_core_web_sm')
doc = nlp('I have flown to Moscow. Now I am flying to Frisco.')

for token in doc:
    print(token.text, token.pos_, token.dep_)