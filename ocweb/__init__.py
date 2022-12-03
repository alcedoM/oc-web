# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import LoginManager

app = Flask('ocweb')
app.config.from_pyfile('config.py')
app.secret_key = 'secret string'

db = SQLAlchemy(app)
ckeditor = CKEditor(app)
login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_admin(user_id):
    from ocweb.models import Admin
    user = Admin.query.get(int(user_id))
    return user


from ocweb import views, errors, commands
