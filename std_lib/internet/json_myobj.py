#! /usr/bin/env python3 

class MyClass:

    def __init__(self, s: str) -> None:
        self.s = s 

    def __repr__(self) -> str:
        return f'<MyClass({self.s})'

        