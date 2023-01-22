#! /usr/bin/env python3 

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    word = 'word!'
    return f'Hello {word}'

if __name__ == '__main__':
    app.run(debug=True)