from src.exceptions import ZeroProductsQuantity
from src.order import BaseOrder
from src.product import Product


class Category(BaseOrder):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        super().__init__(name, description)
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_amount = 0
        for amount in self.__products:
            total_amount += amount.quantity
        return f"{self.name}, количество продуктов: {total_amount} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductsQuantity(
                        "Нельзя добавить товар с нулевым количеством"
                    )
            except ZeroProductsQuantity as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products_to_list(self):
        return self.__products

    def get_info(self) -> str:
        return (
            f"Категория: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Дата создания: {self.created_at}\n"
            f"Количество товаров: {len(self.__products)}"
        )

    def middle_price(self):
        try:
            return round(
                sum(product.price for product in self.__products)
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0
