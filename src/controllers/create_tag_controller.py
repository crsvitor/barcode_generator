from typing import Dict
from barcode import Code128
from barcode.writer import ImageWriter

class CreateTagController:
    def execute(self, product_code: str):
        tag_path = self.__create_tag(product_code=product_code)
        return self.__format_response(tag_path=tag_path)

    def __create_tag(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        tag_path = f'tags/{tag}'
        tag.save(tag_path)
        return tag_path

    def __format_response(self, tag_path: str) -> Dict:
        return {
            "data": {
                "type": "Tag image",
                "count": 1,
                "path": tag_path
            }
        }
