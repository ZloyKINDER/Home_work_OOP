import pytest


def test_smartphone(smartphone_one, smartphone_two, smartphone_three, lawngrass_one, lawngrass_two):
    assert smartphone_one.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_one.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_one.price == 180000.0
    assert smartphone_one.quantity == 5
    assert smartphone_one.efficiency == 95.5
    assert smartphone_one.model == "S23 Ultra"
    assert smartphone_one.memory == 256
    assert smartphone_one.color == "Серый"

    assert smartphone_two.name == "Iphone 15"
    assert smartphone_two.description == "512GB, Gray space"
    assert smartphone_two.price == 210000.0
    assert smartphone_two.quantity == 8
    assert smartphone_two.efficiency == 98.2
    assert smartphone_two.model == "15"
    assert smartphone_two.memory == 512
    assert smartphone_two.color == "Gray space"

    assert smartphone_three.name == "Xiaomi Redmi Note 11"
    assert smartphone_three.description == "1024GB, Синий"
    assert smartphone_three.price == 31000.0
    assert smartphone_three.quantity == 14
    assert smartphone_three.efficiency == 90.3
    assert smartphone_three.model == "Note 11"
    assert smartphone_three.memory == 1024
    assert smartphone_three.color == "Синий"


def test_smartphone_add(smartphone_one, smartphone_two):
    assert smartphone_one + smartphone_two == 2580000.0


def test_smartphone_error(smartphone_one):
    with pytest.raises(TypeError):
        result = smartphone_one + 1