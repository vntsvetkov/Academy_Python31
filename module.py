""" День 3. Объектно-ориентированное программирование.
Статические поля и методы"""
from math import pi

"""
1. Статический метод - метод, который работает как обычная функция.
Этот метод не влияет на состояние класса и объекта.
Для вызова статического метода не обязательно создавать экземпляр класса

2. Статические поля (переменные класса) - переменные, объявленная внутри класса,
но вне метода инициализации. К статической переменной можно обращаться 
непосредственно от самого класса или от объекта этого класса

3. Методы класса - методы, которые можно вызывать от самого класса.
Этот метод не может влиять на состояние объекта, но влияет на состояние класса
Основная задача 
"""


class Circle:

    __color: str = '#FFFFFF'  # цвет фигуры
    __count: int = 0  # количество экземпляров объекта

    def __init__(self, x: int, y: int, radius: float):
        self.__x = x
        self.__y = y
        self.__radius = self.__validate_radius(radius)
        Circle.__count += 1

    def obj_set_color(self, value):
        self.__color = value

    def obj_get_color(self):
        return self.__color

    @classmethod
    def create_circle_by_diameter(cls, x: int, y: int, diameter: float):
        radius = cls.__validate_radius(diameter / 2)
        return cls(x, y, radius)

    @classmethod
    def get_color(cls):
        return cls.__color

    @classmethod
    def set_color(cls, value: str):
        cls.__color = value

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return pi * self.__radius ** 2

    @staticmethod
    def get_count():
        return Circle.__count

    @staticmethod
    def __validate_radius(radius: float):
        if radius < 0:
            raise ValueError("Радиус окружности не может быть отрицательным")
        return radius


class ConverterCurrency:

    dollar_rate: float = 94.28
    euro_rate: float = 100.36

    @staticmethod
    def rub_to_dollar(rub: float):
        return rub / ConverterCurrency.dollar_rate

    @staticmethod
    def rub_to_euro(rub: float):
        return rub / ConverterCurrency.euro_rate


