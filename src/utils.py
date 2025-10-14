import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path: str = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        product_data: Any = json.load(file)
    return product_data


def create_objects_from_json(data: Any) -> list:
    categories: list = []
    for category in data:
        products: list = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
