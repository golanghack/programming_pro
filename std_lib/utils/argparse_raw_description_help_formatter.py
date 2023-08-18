#! /usr/bin/env python3 

import argparse

parser = argparse.ArgumentParser(
    add_help=True, 
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=""" 
    description 
            not 
                wrapped""" 
)

parser.add_argument('a', action='store_true',
                            help="""Argument help is wrapped""",)
parser.print_help()
