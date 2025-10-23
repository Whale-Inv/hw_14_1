import pytest


def test_lawngrass_init(test_lawn_grass_1):
    assert test_lawn_grass_1.name == "Газонная трава"
    assert test_lawn_grass_1.description == "Элитная трава для газона"
    assert test_lawn_grass_1.price == 500.0
    assert test_lawn_grass_1.quantity == 20
    assert test_lawn_grass_1.country == "Россия"
    assert test_lawn_grass_1.germination_period == "7 дней"
    assert test_lawn_grass_1.color == "Зеленый"


def test_lawngrass_add(test_lawn_grass_1, test_lawngrass_2):
    assert test_lawn_grass_1 + test_lawngrass_2 == 16750


def test_lawngrass_add_error(test_lawn_grass_1, test_smartphone_1):
    with pytest.raises(TypeError):
        assert test_lawn_grass_1 + test_smartphone_1
