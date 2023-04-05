from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list):
        business_dict = {}
        oldest_manufacturing_date = datetime.max.date()
        closest_to_expire = datetime.max.date()

        for product in list:
            manufacturing_date_converted = datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ).date()
            expiring_date_converted = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if manufacturing_date_converted < oldest_manufacturing_date:
                oldest_manufacturing_date = manufacturing_date_converted

            if (
                expiring_date_converted < closest_to_expire
                and expiring_date_converted >= datetime.now().date()
            ):
                closest_to_expire = expiring_date_converted

            if product["nome_da_empresa"] not in business_dict:
                business_dict[product["nome_da_empresa"]] = 0
            business_dict[product["nome_da_empresa"]] += 1

        more_products = max(business_dict, key=business_dict.get)
        oldest_manufacturing_str = (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
        )
        closest_to_expire_str = (
            f"Data de validade mais próxima: {closest_to_expire}\n"
        )
        more_products_str = f"Empresa com mais produtos: {more_products}"

        return (
            oldest_manufacturing_str
            + closest_to_expire_str
            + more_products_str
        )
