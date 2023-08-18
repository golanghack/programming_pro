#! /usr/bin/env python3 

import asyncio
from threading import Thread
from gui_for_stress_testing import LoadTester

class TheadedEventLoop(Thread):
    """New class of Thread for asyncio abstract loop."""
    
    def __init__(self, loop: asyncio.AbstractEventLoop): 
        super().__init__()
        self._loop = loop
        self.daemon = True
        
    def run(self):
        self._loop.run_forever()

loop = asyncio.new_event_loop()
asyncio_thread = TheadedEventLoop(loop)

# start new thread
asyncio_thread.start()

app = LoadTester(loop)
app.mainloop()