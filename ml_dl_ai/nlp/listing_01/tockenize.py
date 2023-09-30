#! /usr/bin/env python3

"""Example tockenization"""

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I love you, Donna!')
print([w.text for w in doc])