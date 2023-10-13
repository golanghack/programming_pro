#! /usr/bin/env python3 

from asyncio import Future

my_future = Future()
print(f'my_future ready? -> {my_future.done()}')

my_future.set_result(42)
print(f'my_future ready? -> {my_future.done()}')

print(f'Which result saving in my_future? -> {my_future.result()}')

