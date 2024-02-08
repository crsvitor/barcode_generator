from flask import jsonify
from barcode import Code128
from barcode.writer import ImageWriter

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class CreateTagView:
    def execute(self, http_request: HttpRequest):
        body_request = http_request.body
        product_code = body_request["product_code"]

        tag = Code128(product_code, writer=ImageWriter())
        tag_path = f'tags/{tag}'
        tag.save(tag_path)

        http_response = HttpResponse(status_code=200, body={ "tag_path": tag_path })
        return jsonify(http_response.body), http_response.status_code
