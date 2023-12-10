# -*- coding: utf-8 -*-
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


def create_app(db_url):
    # Инициализация Flask приложения
    usApp = Flask(__name__)
    # Указание конфигурации Flask-SQLAlchemy для работы с БД
    usApp.config['SQLALCHEMY_DATABASE_URI'] = db_url
    usApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return usApp


userApp = create_app('postgresql://postgres:klotorol159@127.0.0.1:5432/n')


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
# Создание сессии для БД
db = SQLAlchemy(userApp)
# Инициализация классов БД

from userApp.database import *


# Создание таблиц БД в соответствии с описанными классами
with userApp.app_context():
    db.create_all()

# Инициализация интерфейсов
from userApp.interfaces import *

# Указание конфигурации Flask приложения
userApp.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or os.urandom(24)


def get_private(x):
    if x == 'Частная организация' or x=='Частная':
        return True
    return False


