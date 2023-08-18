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
import json
import os
import re 
import subprocess
import sys 

UTF8 = 'utf-8'

TRANSFORM, SUMMARIZE = ('TRANSFOM', 'SUMMARIZE')
Code = collections.namedtuple('Code', 'name code kind')

def main():
    genome = 3 * GENOME 
    for i, code in enumerate(CODE):
        context = dict(genome=genome, target='G[AC]{2}TT', replace='TCGA')
        execute(code, context)
        
if sys.version_info[2:] > (3, 1):
    def execute(code: str, context: str):
        module, offset = create_module(code.code, context)
        with subprocess.Popen([sys.executable, '-'], stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            communicate(process, code, module, offset)
            
else:
    def execute(code: str, context: str):
        module, offset = create_module(code.code, context)
        process =  subprocess.Popen([sys.executable, '-'], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        communicate(process, code, module, offset)
        
def create_module(code: str, context: str):
    """Creating dinamic module"""
    
    lines = ['import json', 'result = error = None']
    for key, value in context.items():
        lines.append(f'{key} = {value!r}')
    offset = len(lines) + 1
    output_line = '\nprint(json.dumps((result, error)))'
    return '\n'.join(lines) + '\n' + code + output_line, offset


def communicate(process: str, code: str, module: str, offset: str):
    stdout, stderr = process.communicate(module.encode(UTF8))
    if stderr:
        stderr = stderr.decode(UTF8).lstrip().replace(', in <module>', ':')
        stderr = re.sub(', line (\d+)', lambda match: str(int(match.group(1)) - offset), stderr)
        print(re.sub(r'File."[^"]+?"', f'"{code.name}" as an error on line ', stderr))
    if stdout:
        result, error = json.loads(stdout.decode(UTF8))
        handle_result(code, result, error)
        return
    print(f'"{code.name}" produced no result')
    
def handle_result(code: str, result: str, error: str) -> str:
    if error is not None:
        print(f'"{code.name}" error -> {error}')
    if result is None:
        print(f'"{code.name}" produced no result')
    if code.kind == TRANSFORM:
        genome = result
        try:
            print(f'"{genome}" produced a genome of lenght {len(genome)}')
        except TypeError as err:
            print(f'"{code.name}" error -> expected a sequanse result -> {err}')
    if code.kind == SUMMARIZE:
        print(f'"{code.name}" produced a result of {result}')
    print()
    

CODE = (
    Code("Count",
"""
import re
matches = re.findall(target, genome)
if matches:
    result = len(matches)
else:
    error = f"'{target}' not found"
""", SUMMARIZE)
,
    Code("Replace",
"""
import re
result, count = re.subn(target, replace, genome)
if not count:
    error = f"no '{target}' replacements made"
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
    error = f"'{target}' not found"
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


if __name__ == "__main__":
    main()
            
            