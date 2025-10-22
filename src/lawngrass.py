from src.product import Product


class LawnGrass(Product):
    """ Класс для добавления категории Трава газонная """
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)

        raise TypeError
