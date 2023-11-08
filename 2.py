""""""

""" 
Принцип открытости/закрытости (OCP)
Программные сущности (классы) должны быть открыты для расширения,
но закрыты для модификации

"""

# Пример 1. Класс автомобиль


class Car:

    def __init__(self, model: str):
        self.model = model

    def drive(self, distance: float):
        raise NotImplementedError


class PetrolCar(Car):

    def drive(self, distance: float):
        # какие-то вычисления
        print(f"Расход бензина составил ...")


class ElectricCar(Car):

    def drive(self, distance: float):
        # какие-то вычисления
        print("Расход электроэнергии составил ...")


# Пример 2. класс Фигура

class Shape:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def area(self):
        raise NotImplementedError


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
