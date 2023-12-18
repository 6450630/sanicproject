# -*- coding: utf-8 -*-

from sanic.response import json


class SetStatusCode():
    def __init__(self) -> None:
        pass
    
    def success(self,data):
        if data:
            pass
        return