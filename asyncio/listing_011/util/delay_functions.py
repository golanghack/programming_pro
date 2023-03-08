#! /usr/bin/env python3 
"""This module for delay functions."""

import asyncio

async def delay(delay_seconds: int) -> int:
    """Function sleeping delay for coroutines."""
    
    print(f'I`m sleeping on -> {delay_seconds} sec.')
    await asyncio.sleep(delay_seconds)
    print(f'sleep current -> {delay_seconds} sec finished.')
    return delay_seconds
