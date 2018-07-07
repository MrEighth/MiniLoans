# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from .routes import router
from config import config


mail = Mail()
db = SQLAlchemy()


# 工厂函数延迟创建实例, 外部先初始化config
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)

    # 注册路由, 与app分开定义
    app.register_blueprint(router)

    return app
