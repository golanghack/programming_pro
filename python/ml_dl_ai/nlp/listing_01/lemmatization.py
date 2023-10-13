#! /usr/bin/env python3 

"""Lemmatization"""

import spacy as sp 
nlp = sp.load('en_core_web_sm')
doc = nlp(u'Hello boys! How are you?')
for token in doc:
    print(token.text, token.lemma_)