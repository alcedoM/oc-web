import click

from ocweb import app, db
from ocweb.models import *


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    admin = Admin.query.first()
    if admin is not None:
        click.echo('Updating user...')
        admin.username = username
        admin.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        admin = Admin(username=username)
        admin.set_password(password)  # 设置密码
        db.session.add(admin)
        db.session.commit()  # 提交数据库会话
    click.echo('Done.')
