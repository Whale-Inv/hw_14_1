import pytest


def test_smartphone_init(test_smartphone_1):
    assert test_smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone_1.price == 180000.0
    assert test_smartphone_1.quantity == 5
    assert test_smartphone_1.efficiency == 95.5
    assert test_smartphone_1.model == "S23 Ultra"
    assert test_smartphone_1.memory == 256
    assert test_smartphone_1.color == "Серый"


def test_smartphone_add(test_smartphone_1, test_smartphone_2):
    assert test_smartphone_1 + test_smartphone_2 == 2580000


def test_smartphone_add_error(test_smartphone_1, test_lawn_grass_1):
    with pytest.raises(TypeError):
        assert test_smartphone_1 + test_lawn_grass_1
