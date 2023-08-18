#! /usr/bin/env python3

import typer 
from typing import Optional

def full_output(name: str) -> str:
    return f'Hello {name}'

app = typer.Typer()

@app.command()
def main(name: Optional[str]=typer.Argument('World')):
    print(full_output(name))
    
if __name__ == '__main__':
    app()