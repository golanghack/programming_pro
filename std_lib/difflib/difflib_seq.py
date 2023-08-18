#! /usr/bin/env python3 

import difflib

s1 = [1, 2, 3, 5, 6, 4]
s2 = [2, 3, 5, 4, 6, 1]

print('<--Initial data -->')
print('s1 =', s1)
print('s2 =', s2)
print('s1 == s2 -> ', s1 == s2)
print()

matcher = difflib.SequenceMatcher(None, s1, s2)
for tag, i1, i2, j1, j2 in reversed(matcher.get_opcodes()):
    if tag == 'delete':
        print(f'remove {s1[i1:i2], i1, i2}')
        print(f'before =', s1)
        del s1[i1:i2]
    elif tag == 'equal':
        print(f's1[{i1}:{i2}] and s2[{j1}:{j2}] are the same')
    elif tag == 'insert':
        print(f'Insert {s2[j1:j2]} from s2[{j1}:{j2}] into s1 at {i1}')
        print('before =', s1)
        s1[i1:i2] = s2[j1:j2]
    elif tag == 'replace':
        print(f'Replace {s1[i1:i2]} from s1[{i1}:{i2}] with {s2[j1:j2]} from s2[{j1}:{j2}]')
        print('before =', s1)
        s1[i1:i2] = s2[j1:j2]
    print('after =', s1, '\n')
print('s1 == s2:', s1 == s2)
        