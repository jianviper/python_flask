# -*- coding:utf-8 -*-
__metaclass__ = type
from flask import Flask
from flask_wtf import FlaskForm
import wtforms as wtfs


class ApiForm(FlaskForm):
	name = wtfs.StringField('what is your name?', validators=[wtfs.validators.DataRequired()])
	##text = wtfs.StringField('', validators=[wtfs.validators.DataRequired()])
	submit = wtfs.SubmitField('submit')
