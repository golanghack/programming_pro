#! /usr/bin/env python3 

import argparse
import asyncio
import logging
import sys 
import time
import warnings

parser = argparse.ArgumentParser('debugging asyncio')
parser.add_argument(
    '-v', 
    dest='verbose', 
    default=False, 
    action='store_true',
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)7s -> %(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('')

async def inner():
    LOG.info('inner starting')
    # Use pause blocking for simulation function work
    time.sleep(.1)
    LOG.info('inner completed')


async def outer(loop):
    LOG.info('outer starting')
    await asyncio.ensure_future(loop.create_task(inner()))
    LOG.info('outer completed')

event_loop = asyncio.get_event_loop()
if args.verbose:
    LOG.info('enabling debugging')

    # Turn off debug
    event_loop.set_debug(True)

    # Low limit for work of function
    event_loop.slow_callback_duration = .001

    # Pushing all errors async resources
    warnings.simplefilter('always', ResourceWarning)

LOG.info('entering event loop')
event_loop.run_until_complete(outer(event_loop))
event_loop.close()