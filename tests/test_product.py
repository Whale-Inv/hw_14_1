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
