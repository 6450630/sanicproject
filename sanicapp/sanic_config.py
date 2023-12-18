# -*- coding: utf-8 -*-

from sanic.config import Config


class MyConfig(Config):
    CORS_ALLOW_HEADERS = '*'
    DB_HOST = 'localhost'
    DB_KWARGS = dict(pool_class=NullPool,)