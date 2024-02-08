from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.create_tag_controller import CreateTagController

class CreateTagView:
    def execute(self, http_request: HttpRequest):
        body_request = http_request.body
        product_code = body_request["product_code"]

        create_tag_controller = CreateTagController()
        created_tag = create_tag_controller.execute(product_code=product_code)

        return HttpResponse(status_code=200, body=created_tag)
