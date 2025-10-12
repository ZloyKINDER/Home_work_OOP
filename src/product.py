class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price >= new_price:
            self.__price = new_price
        else:
            access = input("Подтвердите цену: y = да, n = нет: ")
            print(access)
            if access == "y":
                self.__price = new_price
            else:
                print("Нет так нет")
