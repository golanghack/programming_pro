#! /usr/bin/env python3 

import asyncio

async def phase(i):
    print(f'in phase -> {i}')
    try:
        await asyncio.sleep(.1 * i)
    except asyncio.CancelledError:
        print(f'phase {i} canceled')
        raise
    else:
        print(f'done with phase {i}')
        return f'phase {i} result'

async def main(num_phases):
    print('starting main')
    phases = [
        phase(i) for i in range(num_phases)
    ]
    print('waiting 0.1 for phases to complete')
    completed, pending = await asyncio.wait(phases, timeout=.1)
    print(f'{len(completed)} completed and {len(pending)} pending')

    # cancel tasks for execeptions error before exit 
    if pending:
        print('canceling tasts')
        for t in pending:
            t.cancel()
    print('exiting main')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()