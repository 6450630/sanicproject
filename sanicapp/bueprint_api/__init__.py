
from sanic import Blueprint
from .api_test1 import at
from .questions import questions_api

test = Blueprint.group(at,  url_prefix="/test")
questions_group_api = Blueprint.group(questions_api,  url_prefix="/questions")
api = Blueprint.group(test, questions_group_api, url_prefix="/api")