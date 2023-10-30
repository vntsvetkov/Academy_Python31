""" День 5. Объектно-ориентированное программирование.
Абстрактные классы и методы """

from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self):
        raise NotImplementedError("Ошибка расчета площади")

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Ошибка расчета периметра")


class Circle(Figure):
    name = "Окружность"
    from math import pi

    def __init__(self, x: int, y: int, radius: float):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def area(self):
        return Circle.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * Circle.pi * self.__radius


class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, x: int, y: int, w: float, h: float):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    def area(self):
        return self.__h * self.__w

    def perimeter(self):
        return 2 * (self.__h + self.__w)


""" 
Задача 1. Реализовать абстрактный класс Транспорт.
Создать 2 наследника: автомобиль и мотоцикл.
Используя один из этих классов необходимо проехать/не проехать
некоторое расстояние исходя из характеристик транспорта.
Перед началом движения необходимо завести двигатель и
проверить сможет/не сможет транспорт проехать указанное 
расстояние с имеющимся запасом топлива.
"""


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        """ Завести двигатель """
        ...

    @abstractmethod
    def stop_engine(self):
        """ Остановить двигатель"""
        ...

    @abstractmethod
    def check_fuel(self, distance: float):
        """ Проверка топлива """
        ...

    @abstractmethod
    def drive(self, distance: float):
        ...

    @classmethod
    @abstractmethod
    def change_consumption(cls, value):
        ...


class Car(Transport):
    __consumption: float = 2.0  # расход в л./км.
    status_engine = False  # состояние двигателя

    def __init__(self, model: str, tank: float):
        self.__model = model
        self.__tank = tank  # объем бака

    @classmethod
    def change_consumption(cls, value: float):
        if value <= 0:
            raise ValueError("Расход топлива не может быть ...")
        cls.consumption = value

    def start_engine(self):
        if not self.status_engine:
            self.status_engine = True
            print("Двигатель заведен")
        else:
            print("Двигатель уже заведен")

    def stop_engine(self):
        if self.status_engine:
            self.status_engine = False
            print("Двигатель выключен")
        else:
            print("Двигатель уже выключен")

    def check_fuel(self, distance: float) -> bool:
        return distance * self.__consumption <= self.__tank

    def drive(self, distance: float):
        if not self.status_engine:
            print("Двигатель не заведен")
        elif not self.check_fuel(distance):
            print("Не хватает топлива в баке")
        else:
            print("Поездка прошла успешно")
            self.__tank = self.__tank - distance * self.__consumption


class CargoCar(Car):
    ...


class Bike(Transport):
    consumption: float = 2  # расход в л./км.
    status_engine = False  # состояние двигателя

    def __init__(self, model: str, tank: float):
        self.__model = model
        self.__tank = tank  # объем бака

    @classmethod
    def change_consumption(cls, value: float):
        if value <= 0:
            raise ValueError("Расход топлива не может быть ...")
        cls.consumption = value

    def start_engine(self):
        if not self.status_engine:
            self.status_engine = True
            print("Двигатель заведен")
        else:
            print("Двигатель уже заведен")

    def stop_engine(self):
        if self.status_engine:
            self.status_engine = False
            print("Двигатель выключен")
        else:
            print("Двигатель уже выключен")

    def check_fuel(self, distance: float) -> bool:
        return distance * self.consumption <= self.__tank

    def drive(self, distance: float):
        if not self.status_engine:
            print("Двигатель не заведен")
        elif not self.check_fuel(distance):
            print("Не хватает топлива в баке")
        else:
            print("Поездка прошла успешно")
            self.__tank = self.__tank - distance * self.consumption
