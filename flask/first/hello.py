#! /usr/bin/env python3 

from flask import Flask 
from flask import request 

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your brouser is {user_agent}</p>'
@app.route('/user/<name>')
def user(name: str) -> str:
    return f'<h1>Hello, {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)