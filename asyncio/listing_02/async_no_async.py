#! /usr/bin/env python3 

async def coroutine_add_one(number: int) -> int:
    return number + 1

def add_one(number: int) -> int:
    return number + 1 

function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f'Result of function -> {function_result}, and type -> {type(function_result)}')
print()
print(f'Result of coroutine -> {coroutine_result}, and type -> {type(coroutine_result)}')