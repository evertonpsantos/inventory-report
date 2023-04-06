from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith(".json"):
            raise ValueError("'Arquivo inválido'")
        with open(file_path, encoding="utf-8") as file:
            products_json = json.load(file)
            return [product for product in products_json]
