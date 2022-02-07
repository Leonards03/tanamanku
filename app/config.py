import os
from datetime import timedelta

import environs
from environs import Env

env = Env()
env.read_env()


class Config(object):
    APP_ENV = 'development'
    Debug = True
    FLASK_RUN_HOST = env.str('FLASK_RUN_HOST')
    FLASK_RUN_PORT = env.str('FLASK_RUN_PORT')

    DB_HOST = env.str('DB_HOST', '127.0.0.1')
    DB_USERNAME = env.str('DB_USERNAME', 'root')
    DB_PASSWORD = env.str('DB_PASSWORD', '')
    DB_NAME = env.str('DB_NAME', 'tanamanku_db')
    DB_PORT = env.str('DB_PORT', '3306')
    MYSQL_UNIX_SOCKET = 'TCP'

    MAX_CONTENT_LENGTH = 16 * 1000 * 1000  # Maximum file size uploaded is 16MB
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    SECRET_KEY = env.str('SECRET_KEY', 'tanamanku-community')

    MAIL_USERNAME = env.str('MAIL_EMAIL', 'tanamanku.community@gmail.com')
    MAIL_PASSWORD = env.str('MAIL_PASSWORD', 'pl4ntaeKomunitas')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)


class DevelopmentConfig(Config):
    APP_ENV = 'development'
    Debug = True


class ProductionConfig(Config):
    APP_ENV = 'production'
    Debug = False
