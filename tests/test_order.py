import datetime


def test_order_initial(test_order_init, product):
    assert test_order_init.name == "Заказ Iphone 15"
    assert test_order_init.product == product
    assert test_order_init.quantity == 1
    assert test_order_init.total_cost == 210000.0

    expected_str = (
        f"Заказ: Заказ {test_order_init.product.name}\n"
        f"Товар: {test_order_init.product.name}\n"
        f"Количество: {test_order_init.quantity}\n"
        f"Общая стоимость: {test_order_init.product.price * test_order_init.quantity}"
    )

    assert str(test_order_init) == expected_str


def test_order_get_info(test_order_init, product):
    expected_info = (
        f"Заказ: {test_order_init.name}\n"
        f"Товар: {product.name}\n"
        f"Цена за единицу: {product.price}\n"
        f"Количество: {test_order_init.quantity}\n"
        f"Общая стоимость: {product.price * test_order_init.quantity}\n"
        f"Дата создания: {datetime.datetime.now().replace(microsecond=0)}"
    )

    # Проверяем результат
    assert test_order_init.get_info() == expected_info
