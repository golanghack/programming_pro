#! /usr/bin/env python3 

import spacy as sp 

nlp = sp.load('en_core_web_sm')

doc = nlp('I have flown to Moscow. Now I am flyiong to Frisco.')
for sentense in doc.sents:
    print([word.text for word in sentense if word.dep_ == 'ROOT' or word.dep_ == 'pobj'])