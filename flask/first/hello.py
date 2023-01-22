#! /usr/bin/env python3 

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    word = 'word!'
    return f'Hello {word}'

@app.route('/user/<name>')
def user(name: str) -> str:
    return f'<h1>Hello, {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)