#! /usr/bin/env python3

"""Example tokenization"""

import spacy as sp

nlp = sp.load('en_core_web_sm')
doc = nlp(u'I am tryed')
print([word.text for word in doc])