import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.product_lawngrass import LawnGrass
from src.product_smartphone import Smartphone


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def fourth_product():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def category(first_product, second_product, third_product):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        ),
        products=[first_product, second_product, third_product]
    )


@pytest.fixture
def category_tv(fourth_product):
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        ),
        products=[fourth_product]
    )


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)


@pytest.fixture
def smartphone_one():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_two():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_three():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass_one():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_two():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")



@pytest.fixture
def category_without_products():
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        )
    )