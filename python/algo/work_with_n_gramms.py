#! /usr/bin/env python3 

"""<--ILLUSTRATED WORK WITH N_GRAMMS-->"""

from collections import Counter
import requests
import nltk
nltk.download('punkt')
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

search_term = 'life is a'
split_term = tuple(search_term.split(' '))
search_term_lenght = len(search_term.split(' '))

file = requests.get('http://www.bradfordtuckfield.com/shakespeare.txt')
file = file.text
text = file.replace('\n', '')

file2 = requests.get('http://www.bradfordtuckfield.com/marktwain.txt')
file2 = file2.text
text2 = file2.replace('\n', '')

token = nltk.word_tokenize(text)

def n_gram(token:str, step:int):
    """Building n_gram"""
    
    gram = ngrams(token, step)
    return gram


bigrams = n_gram(token, 2)
trigrams = n_gram(token, 3)
fourgrams = n_gram(token, 4)
fivegrams = n_gram(token, 5)

grams = [bigrams, trigrams, fourgrams, fivegrams]

counter_grams = Counter(grams[search_term_lenght - 1])

matching_terms = [element for element in list(counter_grams.items()) if element[0][:-1] == tuple(split_term)]

if len(matching_terms) > 0:
    frequencies = [item[1] for item in matching_terms]
    maximum = np.max(frequencies)
    highest_term = [item[0] for item in matching_terms if item[1] == maximum][0]
    combined_term = ' '.join(highest_term)
    
    
def search_suggestion(search_term, text):
    token = nltk.word_tokenize(text)
    grams = [ngrams(token,2),ngrams(token,3),ngrams(token,4),ngrams(token,5)]
    split_term = tuple(search_term.split(' '))
    search_term_length = len(search_term.split(' '))
    counted_grams = Counter(grams[search_term_length-1])
    combined_term = 'No suggested searches'
    matching_terms = [element for element in list(counted_grams.items()) if \
    element[0][:-1] == tuple(split_term)]
    if(len(matching_terms) > 0):
        frequencies = [item[1] for item in matching_terms]
        maximum_frequency = np.max(frequencies)
        highest_frequency_term = [item[0] for item in matching_terms if item[1] == \
        maximum_frequency][0]
        combined_term = ' '.join(highest_frequency_term)
    return(combined_term)

