#! /usr/bin/env python3 

import json

name = input("Введите название для Г.П.: ")

with open('config.json', 'r', encoding="utf-8") as f:
    date = json.load(f)

date['name'] = name

with open('config.json', 'w', encoding="utf-8") as f:
    json.dump(date, f, ensure_ascii=False, indent=4)