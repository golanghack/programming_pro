#! /usr/bin/env python3

import re 

bold = re.compile(r'\*{3}(.*?)\*{3}')
text: str = 'Make this ***bold***. This ***too***.'

print('Text -> ', text)
print('Bold -> ', bold.sub(r'<b>\1</b>', text, count=1))