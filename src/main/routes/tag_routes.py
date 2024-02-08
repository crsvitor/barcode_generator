from flask import Blueprint, request
from src.views.http_types.http_request import HttpRequest
from src.views.create_tag_view import CreateTagView

tag_blueprint_routes = Blueprint("tag_routes", __name__)

@tag_blueprint_routes.route("/create_tag", methods=["POST"])
def create_tag():
    create_tag_view = CreateTagView()
    http_request = HttpRequest(body=request.json)

    return create_tag_view.execute(http_request=http_request)
