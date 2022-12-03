# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')


class NewOC(FlaskForm):
    name = StringField('名字', validators=[DataRequired(), Length(1, 50)])
    short_intro = StringField('简介', validators=[Length(0, 70)])
    index_title = StringField('OC页标题', validators=[Length(0, 50)])
    index_body = CKEditorField('OC页文章')
    index_photo = StringField('图片地址', validators=[Length(0, 64)])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 50)])
    password = PasswordField('密码', validators=[DataRequired(), Length(0, 70)])
    submit = SubmitField('登录')
