import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция, которая открывает json-файл"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция, которая создает обьекты из json-файла"""
    categories = []
    for cat in data:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
        cat["products"] = products
        categories.append(Category(**cat))

    return categories
