# -*- coding: utf-8 -*-

from sanic import Sanic
from .sanic_config import MyConfig
from .bueprint_api import test

def CreateApp():
    print(__name__.split('.')[-1])
    app = Sanic(__name__.split('.')[-1], config=MyConfig())
    app.blueprint(test)
    return app
    