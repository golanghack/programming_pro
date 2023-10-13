#! /usr/bin/env python3 

""" 
Problem

You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”)
""" 

from collections import defaultdict

ddl = defaultdict(list)
ddl['one'].append(1)
ddl['one'].append(2)
ddl['two'].append(3)

dds = defaultdict(set)
dds['one'].add(1)
dds['one'].add(2)
dds['two'].add(3)


# usualy dict -> create new example dict for call usualy_dict -> [] this example
usualy_dict = {}
usualy_dict.setdefault('one', []).append(1)
usualy_dict.setdefault('one', []).append(2)
usualy_dict.setdefault('two', []).append(3)


# custom realisation
dict_custom = {}
for key, value in my_parts:
    if key not in dict_custom:
        dict_custom[key] = []
    dict_custom[key].append(value)

# custom realisation with defaultdict
dict_custom = defaultdict(list)
for key, value in my_parts:
    dict_custom[key].append(value)
    

