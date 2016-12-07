# -*- coding:utf-8 -*-
import sqlite3, os
from flask_sqlalchemy import SQLAlchemy
from flask import *

basedir = os.path.abspath(os.path.dirname(__file__))
print 'basedir:%s' % basedir

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

print app.config
db = SQLAlchemy(app)
