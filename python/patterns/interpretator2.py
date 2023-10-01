#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--INTERPRETATOR-->"""

import collections
import sys 

TRANSFORM, SUMMARIZE = ('TRANSFOM', 'SUMMARIZE')
Code = collections.namedtuple('Code', 'name code kind')

def main():
    genome = 3 * GENOME 
    for code in CODE:
        #date for work user
        context = dict(genome=genome, target='G[AC]{2}TT', replace='TCGA')
        execute(code, context)
        
def execute(code: str, context: str) -> str:
    """Work with user code"""
    
    try:
        exec(code.code, globals(), context)
        result = context.get('result')
        error = context.get('error')
        handle_result(code, result, error)
        #catch all Exceptions !!!DONT USED IN PROD!!!
    except Exception as err:
        print(f'"{code.name}" raised exception -> {err}\n')
        
def handle_result(code: str, result: str, error: str) -> str:
    """Building result string genome code"""
    
    if error is not None:
        print(f'"{code.name}" error -> {error}')
    if result is None:
        print(f'"{code.name}" produced no result')
    if code.kind == TRANSFORM:
        genome = result
        try:
            print(f'"{code.name}" produced a genome of lenght {len(genome)}')
        except TypeError as err:
            print(f'"{code.name}" error -> expected a sequence result -> {err}')
    if code.kind == SUMMARIZE:
        print(f'"{code.name}" produced a result of -> {result}')
CODE = (
    Code("Count",
"""
import re
matches = re.findall(target, genome)
if matches:
    result = len(matches)
else:
    error = "'{}' not found".format(target)
""", SUMMARIZE)
,
    Code("Replace",
"""
import re
result, count = re.subn(target, replace, genome)
if not count:
    error = "no '{}' replacements made".format(target)
""", TRANSFORM)
,
    Code("Exception Test",
"""
result = 0
for i in range(len(genome)):
    if genome[i] = "A":
        result += 1
""", SUMMARIZE)
,
    Code("Error Test",
"""
import re
matches = re.findall(target * 5, genome)
if matches:
    result = len(matches)
else:
    error = "'{}' not found".format(target)
""", TRANSFORM)
,
    Code("No Result Test",
"""
# No result
""", TRANSFORM)
,
    Code("Wrong Kind Test",
"""
result = len(genome)
""", TRANSFORM)
,
    Code("Termination Test",
"""
import sys
result = "terminating"
sys.exit()
""", SUMMARIZE)
,
    Code("Length",
"""
result = len(genome)
""", SUMMARIZE)
)


GENOME = """TGTTAGTCGCTCCTCGGTCTAAGACATCAAAGTCGGTCTGCGCGGCTGCTCCCTTAGCGCTG
CATAAGAGCGGGGCAGAGAGAGATAGGCGTTTTGACCGTGGCGAGCAAGGCGCGTCATAGTGTCGCCGTGACTG
ATCCTACTGGGTTCTTGCTACTGCCCGGGTCGCAATCCAAAATCTCCACGCGCTGCCACCCCGAAGAAGATATA
TGTCACTGAATTGTATTGGTAACATAGTCGAATTGGGTTCAGGTAAGTTAGTCGTTTAGCCGCTGCGACAGTGG
TGGAAGGGCGAATAGTGTAAAATTTCGCCTGTTAGTGAACATTATCAGGCTGCCATCGTTGATCGCCCCTCTTA
AACTCAGTCTTAAATGAGTTCCCGCCTAAGGTCATTCGTGCCTTGATGATTGATAGCTCGATTGGTCCCTTATG
AAACCGGACCAGAAATGTACCCGCTGAACCGGTGTCATAAGTGTCGCCGTCCCTACGATCGACACTTCCTGAGC
ACGAACGATTTGCGACGCTGTAATGCCACGAGGACTGCATTGAAGATTTTTTGTCCTAGGTGTATGTGCTTCTC
AGGAAGATGCACTACGCACTCCCCTTATCACGGGTGTGACCATCAGGTAGCGTAGGAAGATTAAGACCGCGTAA
CTATCCCTTTCCGTCGCACTCCGACGTCTCAGCACATGTGCGGGGGCCCCTAATTGAGAAACAGTCCATGGTTG
TCCGTAAGTTTCGGAAATCAACTTCACTGCTAGATGGTTGGACGCCAAGGCTCAATAGGTTGGACTCTAAGAAG
""".replace("\n", "")


if __name__ == '__main__':
    main()