# -*- coding:utf-8 -*-
from main import app
from flask import current_app

print app.url_map

app_ctx=app.app_context()
app_ctx.push()
print current_app.__name__