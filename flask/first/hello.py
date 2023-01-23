#! /usr/bin/env python3 

from flask import Flask 
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    word = 'word!'
    return f'Hello {word}'

@app.route('/user/<id>')
def user(id: int) -> str:
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Hello, {user.name}'

if __name__ == '__main__':
    app.run(debug=True)