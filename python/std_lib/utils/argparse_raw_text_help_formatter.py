#! /usr/bin/env python3 

import argparse

parser = argparse.ArgumentParser(
    add_help=True, 
    formatter_class=argparse.RawTextHelpFormatter,
    description=""" 
                not 
                    wrapped""",
    epilog=""" 
    epilog 
        not 
            wrapped""",
)

parser.add_argument('-a', action='store_true',
                            help="""argument 
                            help is not 
                            wrapped
                            """,
                )
parser.print_help()