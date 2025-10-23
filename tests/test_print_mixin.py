from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    message_1 = capsys.readouterr()
    assert (
        message_1.out.strip()
        == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )

    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    message_2 = capsys.readouterr()
    assert (
        message_2.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    )
