
from sanic import Blueprint
from .api_test1 import at

test = Blueprint.group(at,  url_prefix="/test")