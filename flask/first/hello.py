#! /usr/bin/env python3 

from flask import Flask 
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
   return redirect('https://google.com')

@app.route('/user/<name>')
def user(name: str) -> str:
    return f'<h1>Hello, {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)