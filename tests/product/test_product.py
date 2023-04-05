from inventory_report.inventory.product import Product


def test_cria_produto():
    newProduct = Product(
        1,
        "Xablaunator",
        "Xablau Inc",
        "2023-12-13",
        "2024-12-13",
        "F8HU",
        "a vácuo",
    )

    assert newProduct.nome_do_produto == 'Xablaunator'
    assert newProduct.nome_da_empresa == 'Xablau Inc'
    assert newProduct.data_de_fabricacao == "2023-12-13"
    assert newProduct.data_de_validade == "2024-12-13"
    assert newProduct.numero_de_serie == "F8HU"
    assert newProduct.instrucoes_de_armazenamento == "a vácuo"
