from typing import Dict
from src.drivers.bar_code_handler import BarcodeHandler

class CreateTagController:
    def execute(self, product_code: str):
        tag_path = self.__create_tag(product_code=product_code)
        return self.__format_response(tag_path=tag_path)

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        tag_path = barcode_handler.create_barcode(product_code=product_code)
        return tag_path

    def __format_response(self, tag_path: str) -> Dict:
        return {
            "data": {
                "type": "Tag image",
                "count": 1,
                "path": tag_path
            }
        }
