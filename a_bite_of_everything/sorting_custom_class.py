#! /usr/bin/env python3 

from random import randrange
from CustomClass import Foo

random_list = [Foo(randrange(100), randrange(100), randrange(100)) for i in range(6)]

random_list.sort(key=Foo.get_a)
for foo in random_list:
    print(foo)