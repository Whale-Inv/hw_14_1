from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):

    _all_products: dict = {}

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

        Product._all_products[name] = self

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)

        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):

        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if name in cls._all_products:
            existing_product = cls._all_products[name]
            quantity += existing_product.quantity
            if price < existing_product.price:
                price = existing_product.price
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: Any):
        if value <= 0:
            self.__price = self.__price
            print("Цена не должна быть нулевая или отрицательная")

        if 0 < value <= self.__price:
            confirm = input("Вы уверены что хотите снизить цену? y/n \n:")
            if confirm.lower() == "y":
                self.__price = value
