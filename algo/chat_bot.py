#! /usr/bin/env python3 

"""<--CHATBOT-->"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import numpy as np
import nltk, string


alldocuments =[
'Chapter 1. The algorithmic approach to problem solving, including Galileo and baseball.',
'Chapter 2. Algorithms in history, including magic squares, Russian peasant multiplication, and Egyptian methods.',
'Chapter 3. Optimization, including maximization, minimization, and the gradient ascent algorithm.',
'Chapter 4. Sorting and searching, including merge sort, and algorithm runtime.',
'Chapter 5. Pure math, including algorithms for continued fractions and random numbers and other mathematical ideas.',
'Chapter 6. More advanced optimization, including simulated annealing and how to use it to solve the traveling salesman problem.',
'Chapter 7. Geometry, the postmaster problem, and Voronoi triangulations.',
'Chapter 8. Language, including how to insert spaces and predict phrase completions.',
'Chapter 9. Machine learning, focused on decision trees and how to predict happiness and heart attacks.',
'Chapter 10. Artificial intelligence, and using the minimax algorithm to win at dots and boxes.',
'Chapter 11. Where to go and what to study next, and how to build a chatbot.'
]

query = 'I want to read about how to search for items.'
remove_punctuation = dict((ord(char), None) for char in string.punctuation)

stemmer = nltk.stem.porter.PorterStemmer()
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation)))
"""
vctrz = TfidfVectorizer(ngram_range=(1, 1), tokenizer=normalize, stop_words='english')
vctrz.fit(alldocuments)

tfidf_reports = vctrz.transform(alldocuments).todense()
tfidf_question = vctrz.transform([query]).todense()

row_similarities = [1 - spatial.distance.cosine(tfidf_reports[x], tfidf_question) 
                    for x in range(len(tfidf_reports))]
"""
def chatbot(query, allreports):
    clf = TfidfVectorizer(ngram_range=(1, 1), tokenizer=normalize, stop_words='english')
    clf.fit(allreports)
    tfidf_reports = clf.transform(allreports).todense()
    tfidf_question = clf.transform([query]).todense()
    row_similarities = [1 - spatial.distance.cosine(tfidf_reports[x], tfidf_question) 
                        for x in range(len(tfidf_reports))]
    return allreports[np.argmax(row_similarities)]

print(chatbot('Please tell me which chapter I can go to if I want to read about mathematics algorithms. ' ,alldocuments))