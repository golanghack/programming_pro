#! /usr/bin/env python3 

import pickle

class State:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def __repr__(self) -> str:
        return f'State {self.__dict__!r}'
    
class MyClass:
    
    def __init__(self, name: str) -> None:
        print(f'MyClass.__init__({name})')
        self._set_name(name)
        
    def _set_name(self, name: str) -> None:
        self.name = name
        self.computed = name[::-1]
        
    def __repr__(self) -> str:
        return f'MyClass({self.name}) (computed=({self.computed}))'
    
    def __getstate__(self) -> State:
        state = State(self.name)
        print(f'__getstate__ -> {state!r}')
        return state
    
    def __setstate__(self, state: State) -> None:
        print(f'__setstate__ -> ({state!r})')
        self._set_name(state.name)
        
    
inst = MyClass('name here')
print('Before -> ', inst)

dumped = pickle.dumps(inst)
reloaded = pickle.loads(dumped)
print('After -> ', reloaded)