import pytest


def test_lawngrass(smartphone_one, smartphone_two, smartphone_three, lawngrass_one, lawngrass_two):
    assert lawngrass_one.name == "Газонная трава"
    assert lawngrass_one.description == "Элитная трава для газона"
    assert lawngrass_one.price == 500.0
    assert lawngrass_one.quantity == 20
    assert lawngrass_one.country == "Россия"
    assert lawngrass_one.germination_period == "7 дней"
    assert lawngrass_one.color == "Зеленый"

    assert lawngrass_two.name == "Газонная трава 2"
    assert lawngrass_two.description == "Выносливая трава"
    assert lawngrass_two.price == 450.0
    assert lawngrass_two.quantity == 15
    assert lawngrass_two.country == "США"
    assert lawngrass_two.germination_period == "5 дней"
    assert lawngrass_two.color == "Темно-зеленый"


def test_lawngrass_add(lawngrass_one, lawngrass_two):
    assert lawngrass_one + lawngrass_two == 16750.0


def test_lawngrass_error(lawngrass_one):
    with pytest.raises(TypeError):
        result = lawngrass_one + 1
