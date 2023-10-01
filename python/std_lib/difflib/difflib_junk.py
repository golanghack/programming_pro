#! /usr/bin/env python3 

from difflib import SequenceMatcher

def show_results(match):
    print(f'<--a = {match.a}-->')
    print(f'<--b = {match.b}-->')
    print(f'<--size = {match.size}')
    i, j, k = match
    print(f'<--A[a:s+size] = {A[i:i + k]!r}')
    print(f'<--B[b:b+size] = {B[j:j + k]!r}')

A = ' abcd'
B = 'abcd abcd'

print(f'<--A = {A!r}-->')
print(f'<--B = {B!r}-->')

print('\nWithout junk detection -> ')
s1 = SequenceMatcher(None, A, B)
match1 = s1.find_longest_match(0, len(A), 0, len(B))
show_results(match1)

print('\nTreat spaces as junk -> ')
s2 = SequenceMatcher(lambda x: x == '', A, B)
match2 = s2.find_longest_match(0, len(A), 0, len(B))
show_results(match2)