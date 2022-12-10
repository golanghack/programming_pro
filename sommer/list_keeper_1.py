#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--LIST KEEPER 01-->"""

"""
Напишите интерактивную программу обслуживания списков строк
в файлах.
При запуске программа должна создать список всех файлов с расшире
нием .lst в текущем каталоге. Воспользуйтесь функцией os.listdir("."),
чтобы получить список всех файлов, и отфильтруйте из него те файлы,
которые не имеют расширения .lst. В случае отсутствия таких файлов
программа должна попросить пользователя ввести имя файла и доба
вить расширение .lst, если пользователь не сделал этого. Если были
найдены один или более файлов .lst, программа должна вывести их
имена в виде списка пронумерованных строк, начиная с 1. Пользова
телю должно быть предложено ввести номер желаемого файла или 0; в
последнем случае программа должна попросить у пользователя ввести
имя нового файла.
Если был указан существующий файл, программа должна прочитать
его содержимое. Если файл пуст или было указано имя нового файла,
программа должна вывести сообщение «no items are in the list» (спи
сок не содержит элементов).
В случае отсутствия элементов должно быть предложено два варианта
действий: «Add» (добавить) и «Quit» (выйти). Если список содержит
один или более элементов, строки из списка должны выводиться про
нумерованными, начиная с 1, а из доступных действий должны быть
предложены варианты «Add» (добавить), «Delete» (удалить), «Save»
(сохранить) (если файл еще не сохранялся) и «Quit» (выйти). Если
пользователь выбирает действие «Quit» и при этом имеются несохра
ненные изменения, ему должна быть предоставлена возможность со
хранить их. Ниже приводится пример сеанса работы с программой
(большая часть пустых строк, а также заголовок «List Keeper», кото
рый выводится всякий раз при выводе списка, были удалены из лис
тинга):
Choose filename: movies
no items are in the list
[A]dd [Q]uit [a]: a
Add item: Love Actually
1: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: a
Add item: About a Boy
1: About a Boy
2: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]:
Add item: Alien
1: About a Boy
2: Alien
3: Love Actually 
[A]dd [D]elete [S]ave [Q]uit [a]: k
ERROR: invalid choice enter one of 'AaDdSsQq'
Press Enter to continue...
[A]dd [D]elete [S]ave [Q]uit [a]: d
Delete item number (or 0 to cancel): 2
1: About a Boy
2: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: s
Saved 2 items to movies.lst
Press Enter to continue...
1: About a Boy
2: Love Actually
[A]dd [D]elete [Q]uit [a]:
Add item: Four Weddings and a Funeral
1: About a Boy
2: Four Weddings and a Funeral
3: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: q
Save unsaved changes (y/n) [y]:
Saved 3 items to movies.lst
Функция main() должна быть не очень большой (не более 30 строк)
и должна содержать только основной цикл программы. Напишите
функцию, которая будет получать имя нового или существующего
файла (и в последнем случае загружать элементы списка), и функцию,
которая будет выводить перечень доступных действий и принимать
выбор пользователя. Напишите также функции, которые будут добав
лять элемент, удалять элемент, выводить список (либо имен файлов,
либо элементов списка строк), загружать список и сохранять список.
Вставьте в свою программу копии функций get_string() и get_integer()
из программы make_html_skeleton.py или напишите свои собственные
версии.
При выводе элементов списка строк или имен файлов ширина поля
для вывода номеров строк должна быть равна 1, если список содержит
менее десяти элементов, 2 – если в списке менее 100 элементов и 3 –
в противном случае.
Всегда выводите элементы списка в алфавитном порядке, без учета ре
гистра символов, и следите за состоянием списка (за наличием несо
храненных изменений). Действие «Save» должно предлагаться только
при наличии несохраненных изменений, а перед выходом программа
должна спрашивать у пользователя, не желает ли он сохранить изме
нения, только если таковые имеются. Добавление и удаление элемен
тов считаются действиями, которые изменяют список, а после выпол
нения операции сохранения список снова должен считаться неизме
ненным.
"""

import os 

YES = frozenset({'y', 'Y', "yes', 'Yes', 'YES"})

def main():
    dirty = False
    items = []
    
    filename, items = choose_file()
    if not filename:
        print('Cancelled')
        return
    
    while True:
        print('\n<--LIST KEEPER-->\n')
        print_list(items)
        choice = get_choice(items, dirty)
        
        if choice in 'Aa':
            dirty = add_item(items, dirty)
        if choice in 'Dd':
            dirty = delete_item(items, dirty)
        if choice in 'Ss':
            dirty = save_list(filename, items)
        if choice in 'Qq':
            if (dirty and (get_string('Save insaved changes (y/n)', 'yes/no', 'y') in YES)):
                save_list(filename, items, True)
            break
        
def choose_file():
    enter_filename = False
    print('\n<--LIST KEEPER-->\n')
    files = [x for x in os.listdir('.') if x.endswith('.lst')]
    if not files:
        enter_filename = True
    if not enter_filename:
        print_list(files)
        index = get_integer('Specify file`s number (or 0 to create a new one)', 
                            'number', 
                            maximum=len(files), 
                            allow_zero=True)
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]
            items = load_list(filename)
    if enter_filename:
        filename = get_string('Choose filename', 'filename')
        if not filename.endswith('.lst'):
            filename += '.lst'
        items = []
    return filename, items


def print_list(items):
    if not items:
        print('-- no items are in the list ---')
    else:
        #width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, item in enumerate(items):
            print(f'{i + 1:{1 if len(items) < 10 else 2 if len(items) < 100 else 3}}: {item}')
    print()
    
def get_choice(items, dirty):
    while True:
        if items:
            if dirty:
                menu = '[A]dd [D]elete [S]ave [Q]uit'
                valid_choices = 'AaDdSsQq'
            else:
                menu = '[A]dd [D]elete [Q]uit'
                valid_choices = 'AaDdQq'
        else:
            menu = '[A]dd [Q]uit'
            valid_choices = 'AaQq'
        choice = get_string(menu, 'choice', 'a')
        
        if choice not in valid_choices:
            print('ERROR --> invalid choice --enter one of "{0}"'.format(valid_choices))
            input('Press Enter to continue ...')
        else:
            return choice
        
        
        
def add_item(items, dirty):
    item = get_string('Add item', 'item')
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True
    return dirty

def delete_item(items, dirty):
    index = get_integer('Delete item number (or o to cancel)', 'number', maximum=len(items), allow_zero=True)
    if index != 0:
        del items[index - 1]
        return True
    return dirty

def load_list(filename):
    items = []
    fh = None
    try:
        for line in open(filename, encoding='utf8'):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print('ERROR --> failed to load {0}: {1}'.format(filename, err))
        return []
    finally:
        if fh is not None:
            fh.close()
    return items

def save_list(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, 'w', encoding='utf8')
        fh.write('\n'.join(items))
        fh.write('\n')
    except EnvironmentError as err:
        print('ERROR --> failed to save {0}: {1}'.format(filename, err))
        return True
    else:
        print('Saved {0} item{1} to {2}'.format(len(items), ('s' if len(items) != 1 else ''), filename))
        if not terminating:
            input('Press Enter to continue...')
        return False
    finally:
        if fh is not None:
            fh.close()
            

def get_string(message, 
               name='string', 
               default=None, 
               minimum_lenght=0,
               maximum_lenght=8):
    message += ': ' if default is None else ' [{0}]: '.format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_lenght == 0:
                    return ''
                else:
                    raise ValueError('{0} may not be empty'.format(name))
            if not (minimum_lenght <= len(line) <= maximum_lenght):
                raise ValueError('{name} mus be have at least '
                                 '{minimum_lenght} and at most '
                                 '{maximum_lenght} characters'.format(**locals()))
            return line
        except ValueError as err:
            print('Error --> ', err)
            
def get_integer(message,
                name='integer', 
                default=None, 
                minimum=0, 
                maximum=100, 
                allow_zero=True):
    class RangeError(Exception): pass
    message += ': ' if default is None else ' [{0}]: '.format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError('{0} may not be 0'.format(name))
            if not (minimum <= i <= maximum):
                raise RangeError('{name} must be between {minimum} '
                                 'and {maximum} inclusive{0}'.format(' (or 0)' if allow_zero else '', **locals()))
            return i
        except RangeError as err:
            print('ERROR --> ', err)
        except ValueError:
            print('ERROR --> {0} must be an integer'.format(name))

main()