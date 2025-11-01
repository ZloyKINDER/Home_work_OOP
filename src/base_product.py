from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для Product"""

    @abstractmethod
    def __add__(self, other):
        pass
