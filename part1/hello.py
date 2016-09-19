# -*- coding:utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>hello world!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>hello, %s!</h1>' % name

if __name__ == '__main__':
	app.run(debug=True)