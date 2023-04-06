from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        if file_path.endswith(".csv"):
            product_data = CsvImporter.import_data(file_path)

        if file_path.endswith(".json"):
            product_data = JsonImporter.import_data(file_path)

        if file_path.endswith(".xml"):
            product_data = XmlImporter.import_data(file_path)

        if report_type == "simples":
            return SimpleReport.generate(product_data)
        else:
            return CompleteReport.generate(product_data)
