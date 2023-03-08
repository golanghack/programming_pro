#! /usr/bin/env python3 

from .app import TODOapp
from .db import BasicDB

TODOapp(dbmanager=BasicDB('todo.data')).run()
