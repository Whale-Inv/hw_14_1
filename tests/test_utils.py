import json
from unittest.mock import mock_open, patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


def test_read_valid_json():

    mock_file = mock_open(read_data='{"name": "test", "value": 42}')

    with patch("builtins.open", mock_file):
        result = read_json("dummy_path")
        assert result == {"name": "test", "value": 42}


def test_read_non_existent_file():
    with pytest.raises(FileNotFoundError):
        read_json("non_existent_file.json")


def test_read_invalid_json():
    mock_file = mock_open(read_data="{invalid json}")

    with patch("builtins.open", mock_file):
        with pytest.raises(json.JSONDecodeError):
            read_json("dummy_path")


def test_read_empty_file():
    mock_file = mock_open(read_data="")

    with patch("builtins.open", mock_file):
        with pytest.raises(json.JSONDecodeError):
            read_json("dummy_path")


class MockProduct:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class MockCategory:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


@pytest.fixture(autouse=True)
def patch_product_and_category(monkeypatch):
    monkeypatch.setattr("src.product", MockProduct)
    monkeypatch.setattr("src.category", MockCategory)


def test_create_objects_success():
    test_data = [
        {
            "name": "Категория 1",
            "description": "Описание",
            "products": [
                {
                    "name": "Продукт 1",
                    "description": "Описание",
                    "price": 100,
                    "quantity": 10,
                },
                {
                    "name": "Продукт 2",
                    "description": "Описание",
                    "price": 200,
                    "quantity": 5,
                },
            ],
        }
    ]

    categories = create_objects_from_json(test_data)

    # Проверяем результаты
    assert len(categories) == 1
    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Категория 1"
    assert category.description == "Описание"

    # Проверяем продукты
    products = category.products_to_list
    assert len(products) == 2

    product1 = products[0]
    assert isinstance(product1, Product)
    assert product1.name == "Продукт 1"
    assert product1.price == 100
    assert product1.quantity == 10

    product2 = products[1]
    assert isinstance(product2, Product)
    assert product2.name == "Продукт 2"
    assert product2.price == 200
    assert product2.quantity == 5
