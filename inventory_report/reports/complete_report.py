from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        companies_dict = {}
        for product in list:
            if product["nome_da_empresa"] not in companies_dict:
                companies_dict[product["nome_da_empresa"]] = 0
            companies_dict[product["nome_da_empresa"]] += 1

        companies_str = ""
        for company in companies_dict:
            companies_str += f"- {company}: {companies_dict[company]}\n"

        simple_report = SimpleReport.generate(list)
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_str}"
        )
