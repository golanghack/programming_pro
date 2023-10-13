#! /usr/bin/env python3

from asyncio import create_task, get_event_loop, sleep


class Timer:

    def __init__(self, color: bool):
        self.seconds: int = 9
        self.expires: bool = color
        self.color = lambda x: "белых" if color else "чёрных"
        get_event_loop().run_until_complete(self.start_timer())

    async def start_timer(self):
        """Запускает цикл событий"""
        
        await create_task(self.update_timer())

    async def update_timer(self):
        """Ведёт время отсчёта"""

        while self.seconds:
            if self.expires:
                self.seconds -= 1
                await sleep(1)

        assert self.seconds, f"Закончилось время у {self.color}. Противоположный игрок победил"

    def flip_the_timer(self):
        """Меняет положение таймера (активный/деактивный)"""

        switcher = self.expires = not self.expires
        return switcher

    def get_timeset(self) -> str:
        """:return время в виде таймера на электронных часах"""

        return f"{round(self.seconds / 60)}:{self.seconds % 60}"

timer = Timer('blue')
