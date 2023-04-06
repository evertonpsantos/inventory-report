from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("'Arquivo inválido'")
        with open(file_path, encoding="utf-8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
