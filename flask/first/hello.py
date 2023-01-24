#! /usr/bin/env python3 

from flask import Flask 
from flask_script import Manager 

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
    word = 'word!'
    return f'Hello {word}'

if __name__ == '__main__':
    manager.run()