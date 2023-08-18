#! /usr/bin/env python3 

import csv 
from io import StringIO
import textwrap

csv.register_dialect('escaped', 
                     escapechar='\\', 
                     doublequote=False, 
                     quoting=csv.QUOTE_NONE)

csv.register_dialect('singlequote', 
                     quotechar="'", 
                     quoting=csv.QUOTE_ALL)

# generated tests data for knowing dialects 
samples = []
for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    writer.writerow(
        ('coll', 1, '10/10/2023', 
         'Special chars "\' {} to parse'.format(dialect.delimiter))
    )
    samples.append((name, dialect, buffer.getvalue()))
    
# detarmine dialect for sample 
# use for parsing data 
sniffer = csv.Sniffer()
for name, expected, sample in samples:
    print(f'Dialect -> {name}')
    print(f'In -> {sample.rstrip()}')
    dialect = sniffer.sniff(sample, delimiters=',\t')
    reader = csv.reader(StringIO(sample), dialect=dialect)
    print(f'Parsed\n -> {" ".join(repr(r) for r in next(reader))}')