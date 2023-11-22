from copy import copy, deepcopy
from abc import ABC, abstractmethod

"""
Прототип - позволять копию существующего объекта независимо от реализации

"""


class Shape(ABC):

    @abstractmethod
    def copy(self):
        ...


class Rectangle(Shape):

    def __init__(self, w: float, h: float):
        self.__w = w
        self.__h = h

    def copy(self):
        return deepcopy(self)


a = Rectangle(2, 4)
b = a.copy()

print(a)
print(b)

print(a is b)

