# -*- coding: utf-8 -*-
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from ocweb import db


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    short_intro = db.Column(db.String(70))
    index_title = db.Column(db.String(50))
    index_body = db.Column(db.Text)
    index_photo = db.Column(db.String(64))
    articles = db.relationship('Article')
    features = db.relationship('Feature')
    photos = db.relationship('Photo')


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    fvalue = db.Column(db.String(50))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
