#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--MAKE HTML SKELETON-->"""

import datetime
import xml.sax.saxutils

COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All rights reserved."

STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css" href="{0}" />')

HTML_TEMPLATE = """
<?xml version="1.0"?>
<!DOCTYPE html>
<html lang="en">
<head>
<!--{copyright}-->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {stylesheet}
    <title>Document</title>
</head>
<body>
    
</body>
</html>
"""

class CancelledError(Exception): pass

def main():
    information = dict(name=None, 
                       year=datetime.date.today().year, 
                       filename=None, 
                       title=None, 
                       description=None, 
                       keywords=None, 
                       stylesheet=None)
    while True:
        try:
            print("\nMake HTML Skeleton\n")
            populate_information(information)
            make_html_skeleton(**information)
        except CancelledError:
            print("Cancelled")
        if (get_string("\nCreate another (y/n)?", default="y").lower() not in {"y", "yes"}):
            break

def populate_information(information):
    name = get_string("Enter your name (for copyright)", "name", information["name"])
    if not name:
        raise CancelledError()
    year = get_integer("ENter copyright year", "year", information["year"], 2000, datetime.date.today().year + 1, True)
    
    if year == 0:
        raise CancelledError()