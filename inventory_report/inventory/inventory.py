import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        if file_path.endswith(".csv"):
            with open(file_path, encoding="utf-8") as file:
                products_csv = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                product_data = [product for product in products_csv]

        elif file_path.endswith(".json"):
            with open(file_path, encoding="utf-8") as file:
                products_json = json.load(file)
                product_data = [product for product in products_json]

        else:
            with open(file_path, encoding="utf-8") as file:
                product_data = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]

        if report_type == "simples":
            return SimpleReport.generate(product_data)
        else:
            return CompleteReport.generate(product_data)
