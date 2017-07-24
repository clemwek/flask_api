from flask_sqlalchemy import SQLAlchemy
from flask_api.flask_api import app

db = SQLAlchemy(app)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Anything_here'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_api_db'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_flask_api'
