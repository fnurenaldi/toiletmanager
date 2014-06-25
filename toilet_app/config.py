import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    CSRF_ENABLED = True
    HOST = '0.0.0.0'
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'toilet_app.db')
    SECRET_KEY = 'toilet_app_dev'

del os
