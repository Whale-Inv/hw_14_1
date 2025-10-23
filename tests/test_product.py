from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_create():
    product_data = {
        "name": "Iphone 32",
        "description": "4096GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }

    product1 = Product.new_product(product_data)

    assert product1.name == "Iphone 32"
    assert product1.description == "4096GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8


def test_product_existing_higher_price():
    existing_product_data = {
        "name": "Iphone 32",
        "description": "4096GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }

    Product.new_product(existing_product_data)

    low_cost_product_data = {
        "name": "Iphone 32",
        "description": "4096GB, Gray space",
        "price": 21000.0,
        "quantity": 8,
    }

    product12 = Product.new_product(low_cost_product_data)

    assert product12.name == "Iphone 32"
    assert product12.description == "4096GB, Gray space"
    assert product12.price == 210000.0
    assert product12.quantity == 24


def test_product_str(product):
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add(product, product1):
    assert product + product1 == 2114000.0


class TestProductPriceSetter:
    def setup_method(self):
        # Создаем тестовый продукт с начальной ценой
        self.product = Product(
            name="Тестовый продукт", description="Описание", price=1000, quantity=10
        )

    @patch("builtins.input", return_value="y")
    def test_set_lower_price_confirm_yes(self, mock_input):
        # Проверяем снижение цены при подтверждении
        self.product.price = 500
        assert self.product.price == 500

    @patch("builtins.input", return_value="n")
    def test_set_lower_price_confirm_no(self, mock_input):
        # Проверяем что цена не меняется при отказе
        initial_price = self.product.price
        self.product.price = 500
        assert self.product.price == initial_price

    def test_set_zero_price(self):
        # Проверяем установку нулевой цены
        initial_price = self.product.price
        self.product.price = 0
        assert self.product.price == initial_price


def test_product_add_error(product):
    with pytest.raises(TypeError):
        assert product + 1
