from flask import Blueprint, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

tag_blueprint_routes = Blueprint("tag_routes", __name__)

@tag_blueprint_routes.route("/create_tag", methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get("product_code")

    tag = Code128(product_code, writer=ImageWriter())
    tag_path = f'tags/{tag}'
    tag.save(tag_path)

    return jsonify({ "tag_path": tag_path })
