#! /usr/bin/env python3 

from flask import Flask 
from flask import request 
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
   response = make_response('<h1>This is document carries a cockie!</h1>')
   response.set_cookie('answer', '42')
   return response

@app.route('/user/<name>')
def user(name: str) -> str:
    return f'<h1>Hello, {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)