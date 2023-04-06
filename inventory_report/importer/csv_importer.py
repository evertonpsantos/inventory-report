import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("'Arquivo inválido'")
        with open(file_path, encoding="utf-8") as file:
            products_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            return [product for product in products_csv]
