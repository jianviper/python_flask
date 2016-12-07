# -*- coding:utf-8 -*-
import time
from flask import *
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import wtforms as wtfs
from form import ApiForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
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
	return render_template('user.html', name=name)


@app.route('/user_id/<int:id>')
def get_user(id):
	if id != 1:
		abort(404)
	return '<h1>hello,%d!' % id


@app.route('/list/')
def lists():
	lists = ['a', 'b', 'c', 'd', ]
	return render_template('list.html', lists=lists)


@app.route('/form', methods=['GET', 'POST'])
def form1():
	print 'session:%s' % session
	form = ApiForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		session['flag'] = time.time()
		return redirect(url_for('form1'))
	if 'flag' not in session.keys():
		return render_template('form.html', form=form, name=None)
	elif time.time() - float(session['flag']) > 1.0:
		return render_template('form.html', form=form, name=None)
	
	return render_template('form.html', form=form, name=session.get('name'))


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


if __name__ == '__main__':
	app.run(debug=True)
#app.run(debug=True)
