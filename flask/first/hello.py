#! /usr/bin/env python3 
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500 

if __name__ == '__main__':
    app.run()