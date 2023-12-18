# -*- coding: utf-8 -*-
from sanic import Blueprint
from sanic_ext import serializer
from sanicapp.hleper_bin.status_code import SetStatusCode


questions_api = Blueprint("questions") 
ssc = SetStatusCode()

@questions_api.route("/getcategory")
@serializer(ssc.success)
async def get_questions_category(request):
    return {"1":1}


