# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, send_from_directory
from flask_login import login_user, current_user, login_required, logout_user

from ocweb import app, db
from ocweb.forms import RichTextForm, NewOC, LoginForm
from ocweb.models import Character, Admin


@app.route('/')
def index():
    OCset = Character.query.all()
    ProcessedSet = []
    if len(OCset) % 4 == 0:
        row = len(OCset) // 4
    else:
        row = (len(OCset) // 4) + 1
    k = 0
    for i in range(0, row):
        Temp = []
        for j in range(0, 4):
            Temp.append(OCset[k])
            k += 1
            if k == len(OCset):
                break
        ProcessedSet.append(Temp)

    return render_template("index.html", ProcessedSet=ProcessedSet)


@app.route('/oc/<int:oc_id>')
def ocindex(oc_id):
    oc = Character.query.get_or_404(oc_id)
    return render_template("ocindex.html", oc=oc)


@app.route('/new-character', methods=['GET', 'POST'])
@login_required
def createNewOC():
    form = NewOC()
    if form.validate_on_submit():
        name = form.name.data
        short_intro = form.short_intro.data
        index_title = form.index_title.data
        index_body = form.index_body.data
        index_photo = form.index_photo.data
        new_oc = Character(name=name, short_intro=short_intro, index_title=index_title, index_body=index_body,
                           index_photo=index_photo)
        db.session.add(new_oc)
        db.session.commit()
        flash('创建成功', 'info')
        return redirect(url_for('index'))
    return render_template('createNewOC.html', form=form)


@app.route('/uploads/<path:filename>')
def get_photo(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/login-admin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin)
                flash('登陆成功', 'info')
                return redirect(url_for('index'))
            flash('错误的用户名或密码', 'warning')
        else:
            flash('用户不存在','warning')
    return render_template('login.html', form=form)


@app.route('/logout-admin', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('登出成功', 'info')
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404