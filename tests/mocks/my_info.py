#! /usr/bin/env python3 

from pathlib import Path

def home_dir() -> str:
    """Return home path."""
    
    return str(Path.home())

if __name__ == '__main__':
    print(home_dir())