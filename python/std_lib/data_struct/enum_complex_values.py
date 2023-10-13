#! /usr/bin/env python3 

import enum 
class BusStatus(enum.Enum):
    
    new = {
        'num': 7, 
        'transitions': [
            'incomplete', 
            'invalid', 
            'wont_fix', 
            'in_progress',
        ],
    }
    incomlete = {
        'num': 6,
        'transitions': [
            'new', 
            'wont_fix'
        ],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],   
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': [
            'new', 
            'fix_commited'
        ],
    }
    fix_commited = {
        'num': 2, 
        'transitions': [
            'in_progress', 
            'fix_released'
        ],
    }
    fix_released = {
        'num': 1, 
        'transitions': ['new'],
    }
    
    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']
        
    def can_transitions(self, new_state):
        return new_state.name in self.transitions
    
    
    