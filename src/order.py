from abc import ABC, abstractmethod
from datetime import datetime


class BaseOrder(ABC):
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.created_at = datetime.now().replace(microsecond=0)

    @abstractmethod
    def get_info(self) -> str:
        pass


class Order(BaseOrder):
    """
    Класс, в котором будет ссылка на то, какой товар был куплен, количество купленного товара,
    а также итоговая стоимость. В заказе может быть указан только один товар.
    """

    def __init__(self, product, quantity: int):
        super().__init__(f"Заказ {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self):
        return (
            f"Заказ: {self.name}\n"
            f"Товар: {self.product.name}\n"
            f"Количество: {self.quantity}\n"
            f"Общая стоимость: {self.total_cost}"
        )

    def get_info(self) -> str:
        return (
            f"Заказ: {self.name}\n"
            f"Товар: {self.product.name}\n"
            f"Цена за единицу: {self.product.price}\n"
            f"Количество: {self.quantity}\n"
            f"Общая стоимость: {self.total_cost}\n"
            f"Дата создания: {self.created_at}"
        )
