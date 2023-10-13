#! /usr/bin/env python3 

import argparse

class CustomAction(argparse.Action):
    """Customing action""" 

    def __init__(self, 
                option_strings: str, 
                dest: str, 
                nargs: str=None, 
                const: str=None, 
                default: str=None,
                type: str=None, 
                choices: str=None, 
                required: bool=False,
                help: str=None, 
                metavar: str=None):
        argparse.Action.__init__(self, 
                                option_strings=option_strings, 
                                dest=dest, 
                                nargs=nargs, 
                                const=const, 
                                default=default,
                                type=type, 
                                choices=choices,
                                required=required, 
                                help=help,
                                metavar=metavar)
        print('Ininializing...')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print(f'{name} -> {value!r}')
        print()
        return
    
    def __call__(self, 
                parser: str, 
                namespace: str, 
                values: str, 
                option_string: str=None):
        print(f'Processing for -> {self.dest}')
        print(f'parser -> {id(parser)}')
        print(f'values -> {values!r}')
        print(f'option string -> {option_string!r}')

        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        # save results in spacenames use destination
        setattr(namespace, self.dest, values)
        print()


# tests 
parser = argparse.ArgumentParser()
parser.add_argument('-a', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)

results = parser.parse_args(['-a', 'value', '-m', 'multivalue','second'])
print(results)