
from sanic import Blueprint
from sanic.response import json

at = Blueprint("my_blueprint")

@at.route("/")
async def bp_root(request):
    return json({"my": "blueprint"})