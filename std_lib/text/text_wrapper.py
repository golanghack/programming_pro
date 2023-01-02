#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--Text Wrapper-->"""
import textwrap

sample_text = '''
 This program or module is free software: you can redistribute it and/or
 modify it under the terms of the GNU General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version. It is provided for educational
 purposes and is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY                or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 General Public              License for more details.'''
 
 
dedented_text = textwrap.dedent(sample_text).strip()
for width in [10, 5, 20, 30, 45, 60, 90]:
    print(f'{width} Columns --> "\n"')
    print(textwrap.fill(dedented_text, width=width))
    print()