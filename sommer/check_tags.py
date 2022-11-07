#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CHECK TAGS-->"""

import string 
import sys 

class InvalidEntityError(Exception): pass
class InvalidNumericEntityError(InvalidEntityError): pass
class InvalidAlphaEntityError(InvalidEntityError): pass
class InvalidTagContentError(Exception): pass

def parse(filename, skip_on_first_err=False):
    """Parsing file."""
    HEXDIGITS = frozenset('0123456789ABCDEFabcdef')
    NORMAL, PARSING_TAG, PARSING_ENTITY = range(3)
    state = NORMAL
    entity = ""
    fh = None
    
    try:
        fh = open(filename, encoding='utf8')
        errors = False
        for lino, line in enumerate(fh, start=1):
            for column, c in enumerate(line, start=1):
                try:
                    if state == NORMAL:
                        if c == "<":
                            state = PARSING_TAG
                        elif c == "&":
                            entity = ""
                            state = PARSING_ENTITY
                    elif state == PARSING_TAG:
                        if c == ">":
                            state = NORMAL
                        elif c == "<":
                            raise InvalidTagContentError()
                    elif state == PARSING_ENTITY:
                        if c == ";":
                            if entity.startswith("#"):
                                if frozenset(entity[1:]) - HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif not entity.isalpha():
                                raise InvalidAlphaEntityError()
                            entity = ""
                            state = NORMAL
                        else:
                            if entity.startswith("#"):
                                if c not in HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif (entity and c not in string.ascii_letters):
                                raise InvalidAlphaEntityError()
                            entity += c
                except (InvalidEntityError, InvalidTagContentError) as err:
                    if isinstance(err, InvalidNumericEntityError):
                        error = "Invalid numeric entity"
                    elif isinstance(err, InvalidAlphaEntityError):
                        error = "invalid apphabetic entity"
                    elif isinstance(err, InvalidTagContentError):
                        error = "Invalid tag"
                    print(f"ERROR -->{error}<-- in -->{filename}<-- on line -->{lino}<-- column -->{column}<--")
                    if skip_on_first_err:
                        raise
                    entity = ""
                    state = NORMAL
                    errors = True
        if state == PARSING_TAG:
            raise EOFError("missing '>' at end of " + filename)
        elif state == PARSING_ENTITY:
            raise EOFError("missing '<' aat end of " + filename)
        if not errors:
            print("OK", filename)
    except (InvalidEntityError, InvalidTagContentError):
        pass
    except EOFError as err:
        print("ERROR --> enexpected EOF: ", err)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
            
if len(sys.argv) < 2:
    print("Usage -> check_tags.py infile1 [infile2 [...infileN]]")
    sys.exit()
for filename in sys.argv[1:]:
    parse(filename)