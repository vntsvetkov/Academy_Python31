from abc import ABC, abstractmethod

"""
Строитель (builder) - шаблон. который позволяет строить объект пошагово


"""


class Engine(ABC):
    ...


class GasEngine(Engine):
    ...


class Car:

    def __init__(self):
        self.model = None
        self.year = None
        self.color = None
        self.engine = None

    def __str__(self):
        return f"Новый автомобиль {self.model}"


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def get(self):
        ...

    @abstractmethod
    def set_model(self, model):
        ...

    @abstractmethod
    def set_year(self, year):
        ...

    @abstractmethod
    def set_color(self, color):
        ...

    @abstractmethod
    def set_engine(self, engine: Engine):
        ...


class CarBuilder(Builder):
    __car: Car

    def create(self):
        self.__car = Car()

    def get(self):
        return self.__car

    def set_model(self, model):
        self.__car.model = model

    def set_year(self, year):
        self.__car.year = year

    def set_color(self, color):
        self.__car.color = color

    def set_engine(self, engine: Engine):
        self.__car.engine = engine


car_builder = CarBuilder()
car_builder.create()

car_builder.set_model("BMV")
car_builder.set_year(2015)
car_builder.set_color("black")
car_builder.set_engine(GasEngine())

car = car_builder.get()
print(car)

