import pytest


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


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iter(product_filter):
    result = product_filter.__iter__()
    assert result is product_filter

    assert product_filter.index == 0
    assert next(product_filter).name == "Samsung Galaxy S23 Ultra"
    assert next(product_filter).name == "Iphone 15"
    assert next(product_filter).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_filter)


def test_category_add_product_error(first_category):
    with pytest.raises(TypeError):
        assert first_category.add_product(1)