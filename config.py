# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = os.urandom(24)

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/test'  # sql链接

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'mazhuang1994@163.com'
    MAIL_PASSWORD = 'unknown'  # 填写客户端授权码

    FLASKY_MAIL_SUBJECT_PREFIX = '[UncleClub]'
    FLASKY_MAIL_SENDER = MAIL_USERNAME

    FLASKY_ADMIN = 'admin'

    # 继承供其它初始化实现（如有）
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    MAIL_USE_TLS = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': Config
}
