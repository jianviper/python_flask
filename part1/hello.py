# -*- coding:utf-8 -*-
from flask import Flask,request,make_response,redirect,abort,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	#response = make_response('<h1>hello world!</h1>')
	#response.set_cookie('name','linjian')
	#return redirect('http://www.baidu.com')
	#return  response
	return render_template('index.html')

@app.route('/user/<name>/')
def user(name):
	#return '<h1>hello, %s!</h1>' % name
	return render_template('user.html',name=name)

@app.route('/user_id/<int:id>')
def get_user(id):
	if id != 1:
		abort(404)
	return '<h1>hello,%d!' % id

@app.route('/list/')
def lists():
	lists = ['a','b','c','d',]
	return render_template('list.html',lists=lists)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)