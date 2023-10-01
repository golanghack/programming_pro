#! /usr/bin/env python3

import spacy as sp 
from spacy.symbols import LEMMA

nlp = sp.load('en_core_web_sm')
doc = nlp('I want to flying to Frisco')
print([word.text for word in doc])

nlp.get_pipe('attribute_ruler').add([[{'TEXT': 'Frisco'}]], {'LEMMA': 'San Francisco'})
print([word.lemma_ for word in nlp('I want flying to Frisco')])
