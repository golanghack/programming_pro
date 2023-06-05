#! /usr/bin/env python3 

""" 
TASK 

Write a program that reads the contents of a file, parses
each line into words, removes spaces and punctuation from words
and convert them to lowercase
"""

from string import punctuation
import sys 
import os 

def from_text_to_word(text: str) -> str:

    start_word = ''
    text_word = text.translate(str.maketrans('', '', punctuation))
    text_word = text_word.strip(' ')
    text_word = str(text_word).lower()
    text_word = start_word.join(text_word)
    return text_word

def counting_word(text_word: str) -> int:

    count_word = len(text_word)
    return f'\ncount the world -> {count_word}\n'


def main():
    if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"}:
        print("""usage: {0} [infile] [outfile]
if no files are specified reads stdin and writes to stdout;
if one file is specified reads it and writes to stdout;
if both files are specified reads the first and writes to the second
""".format(os.path.basename(sys.argv[0])))
        sys.exit(2)

    file_in, file_out = (sys.stdin, sys.stdout)
    close_in, close_out = (False, False)
    if len(sys.argv) > 1:
        file_in = open(sys.argv[1], encoding="utf8")
        close_in = True
        if len(sys.argv) > 2:
            file_out = open(sys.argv[2], "w", encoding="utf8")
            close_out = True
    text = file_in.read()
    if close_in:
        file_in.close()
    file_out.write(from_text_to_word(text))
    file_out.write(counting_word(text))
    if close_out:
        file_out.close()
    else:
        print()


if __name__ == '__main__':
    main()