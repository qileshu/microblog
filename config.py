#coding=utf-8
import os
# __file__:acquire the path of the module, maybe a relative path 
basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-SQLAlchemy需要，是数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'douban', 'url': 'https://accounts.douban.com/login'},
    { 'name': 'xiami', 'url': 'https://login.xiami.com/member/login'}]
