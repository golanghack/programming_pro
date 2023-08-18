#! /usr/bin/env python3 

from src.contacts import App

def test_loading(benchmark):
    app = App()

    app._contacts = [(f'Name {n}', 'number') for n in range(1000)]
    app.save()

    benchmark(app.load)