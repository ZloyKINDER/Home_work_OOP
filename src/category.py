class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
