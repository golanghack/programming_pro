#! /usr/bin/env python3 

import spacy as sp 

nlp = sp.load('en_core_web_sm')
doc = nlp('I have flown to Moscow. Now I am flying to Madrid.')
for token in doc:
    if token.ent_type != 0:
        print(token.text, token.ent_type)