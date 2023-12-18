# -*- coding: utf-8 -*-

from sanic import Sanic
from .sanic_config import MyConfig
from .bueprint_api import api
from .sanic_context import MySanicContext
from sanic_ext import Extend
from gino.ext.sanic import Gino

def CreateApp():
    print(__name__.split('.')[-1])
    app = Sanic(__name__.split('.')[-1], config=MyConfig(),ctx=MySanicContext())
    app.blueprint(api)
    Extend(app)
    
    db = Gino()
    db.init_app(app)
    return app
    