def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, \
                    но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_to_list) == 3

    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, \
        станет вашим другом и помощником"
    )
    assert len(second_category.products_to_list) == 1

    assert first_category.product_count == 4
    assert second_category.product_count == 4

    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_category_product_list_property(first_category):
    assert (
        first_category.products
        == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"""
    )


def test_category_product_list_setter(first_category, product):
    assert len(first_category.products_to_list) == 3
    first_category.add_product(product)
    assert len(first_category.products_to_list) == 4
