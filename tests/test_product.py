def test_product_init(first_product, second_product, third_product, fourth_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8

    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14

    assert fourth_product.name == '55" QLED 4K'
    assert fourth_product.description == "Фоновая подсветка"
    assert fourth_product.price == 123000.0
    assert fourth_product.quantity == 7


def test_product_add_price(first_product, second_product, third_product):
    assert first_product + second_product == 2580000.0
    assert first_product + third_product == 1334000.0
    assert second_product + third_product == 2114000.0


def test_product_str(first_product, second_product, third_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(second_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(third_product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_price_setter_valid_lower_price(first_product, second_product):
    """
    Испытывает установку более низкой цены, которая должна быть принята.
    """
    new_price = 170000.0
    first_product.price = new_price
    assert first_product.price == new_price
    second_product.price = new_price
    assert second_product.price == 170000.0


def test_price_setter_valid_higher_price_with_confirmation(monkeypatch, first_product):
    """
    Испытывает установку более высокой цены с подтверждением 'y'.
    """
    new_price = 190000.0
    # Имитируем ввод пользователя 'y'
    monkeypatch.setattr("builtins.input", lambda _: "y")
    first_product.price = new_price
    assert first_product.price == new_price


def test_price_setter_valid_higher_price_without_confirmation(monkeypatch, first_product):
    """
    Испытытывает установку более высокой цены без подтверждения (ввод 'n').
    """
    original_price = first_product.price
    new_price = 190000.0
    # Имитируем ввод пользователя 'n'
    monkeypatch.setattr("builtins.input", lambda _: "n")
    first_product.price = new_price
    assert first_product.price == original_price  # Цена не должна измениться


def test_price_setter_price_below_zero(first_product, second_product):
    """
    Испытывает установку более низкой цены, которая должна быть принята.
    """
    new_price = 0.0
    first_product.price = new_price
    assert "Цена не должна быть нулевая или отрицательная"
