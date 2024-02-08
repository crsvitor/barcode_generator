from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.create_tag_view import CreateTagView

tag_blueprint_routes = Blueprint("tag_routes", __name__)

@tag_blueprint_routes.route("/create_tag", methods=["POST"])
def create_tag():
    create_tag_view = CreateTagView()
    http_request = HttpRequest(body=request.json)

    create_tag_response = create_tag_view.execute(http_request=http_request)
    return jsonify(create_tag_response.body), create_tag_response.status_code
