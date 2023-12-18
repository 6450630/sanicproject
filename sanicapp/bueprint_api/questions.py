# -*- coding: utf-8 -*-
from sanic import Blueprint

questions_api = Blueprint("questions") 

@questions_api.route("/getcategory")
async def get_questions_category(request):
    pass


