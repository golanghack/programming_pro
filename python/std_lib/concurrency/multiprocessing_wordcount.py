#! /usr/bin/env python3 

import multiprocessing
import string
from multiprocessing_mapreduce import SimpleMapReduce

def file_to_words(filename: str) -> list:
    """ 
    Read file and return collection of value
    """

    STOP_WORDS = set([
        'a', 'an', 'and', 'are', 'as', 'be', 'by',
        'in', 'is', 'it', 'of', 'or', 'py', 'rst',
        'to', 'with',
                    ])
    TR = str.maketrans({
        p: ' '
        for p in string.punctuation
    })
    print(f'{multiprocessing.current_process().name} reading {filename}')
    output = []

    with open(filename, 'rt') as file:
        for line in file:
            # dont comment
            if line.lstrip().startswith('..'):
                continue
            # blade punctuation
            line = line.translate(TR)
            for word in line.split():
                word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output

def count_words(item):
    """Recombination data to tuple include (word, number into)"""

    word, occurences = item 
    return (word, sum(occurences))

if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.py')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\n<--TOP 20 WORDS NY FREQUENCY-->\n')
    top_20 = word_counts[:20]
    longest = max(len(word) for word, count in top_20)
    for word, count in top_20:
        print('{word:<{len}} -> {count:5}'.format(len=longest + 1, word=word, count=count))
