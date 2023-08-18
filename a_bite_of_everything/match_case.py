#! /usr/bin/env python3 

def handle_command(self, message: str):
    match_message:
        case ['WOW', frequency, times]:
            self.wow(times, frequency)
        case ['NOWOW', angle]:
            self.rotate(angle)
        case _:
            raise InvalidCommand(message)