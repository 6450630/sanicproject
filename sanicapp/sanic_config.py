# -*- coding: utf-8 -*-

from sanic.config import Config

class MyConfig(Config):
    CORS_ALLOW_HEADERS = '*'