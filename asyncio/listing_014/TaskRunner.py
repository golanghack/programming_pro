#! /usr/bin/env python3 

import asyncio 

class TaskRunner:

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.tasks = []

    def add_tasks(self, func):
        self.tasks.append(func)

    async def _run_all(self):
        awaiable_tasks = []

        for task in self.tasks:
            if asyncio.iscoroutinefunction(task):
                awaiable_tasks.append(asyncio.create_task(task()))
            elif asyncio.iscoroutine(task):
                awaiable_tasks.append(asyncio.create_task(task))
            else:
                self.loop.call_soon(task)

        await asyncio.gather(*awaiable_tasks)

    def run(self):
        self.loop.run_until_complete(self._run_all())

if __name__ == '__main__':

    def regular_function():
        print('Regular')
    async def coroutine_function():
        print('Coroutina, sleep')
        await asyncio.sleep(1)
        print('Wake up')
    
    runner = TaskRunner()
    runner.add_tasks(coroutine_function)
    runner.add_tasks(coroutine_function)
    runner.add_tasks(regular_function)

    runner.run()