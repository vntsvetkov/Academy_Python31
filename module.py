""" День 5. Объектно-ориентированное программирование.
Многоуровневое и множественное наследование """

from abc import ABC, abstractmethod
import random


class TrailerMixIn:

    __capacity = 100

    def add_cargo(self, cargo: int):
        """ Добавить груз"""
        self.__capacity -= cargo

    @property
    def capacity(self):
        return self.__capacity


class RadioMixIn:

    __stations = ('Европа+', 'АвтоРадио')

    def play_radio(self):
        print(f"Вы слушаете радио {random.choice(self.__stations)}")


class GroundTransport(ABC):
    """ Абстракция наземного транспорта """

    @abstractmethod
    def drive(self, distance: float):
        ...


class Transport:
    _mileage: float = 0  # начальный пробег равен 0
    _status_engine = False  # двигатель изначально выключен

    def __init__(self, model):
        self.__model = model

    def start_engine(self):
        if not self._status_engine:
            self._status_engine = True
            print("Двигатель заведен")
        else:
            print("Двигатель уже заведен")

    def stop_engine(self):
        if self._status_engine:
            self._status_engine = False
            print("Двигатель выключен")
        else:
            print("Двигатель уже выключен")

    def drive(self, distance):
        raise NotImplementedError


class FuelCar(GroundTransport, Transport, TrailerMixIn):
    __fuel_consumption: float = 0.1  # литра на км.

    def __init__(self, model, tank):
        super().__init__(model)
        self.__tank = tank

    def drive(self, distance: float):
        if not self._status_engine:
            print("Двигатель не заведен")
        elif not self.check_fuel(distance):
            print("Не хватает топлива в баке")
        else:
            print("Поездка прошла успешно")
            self._mileage = self._mileage + distance
            self.__tank = self.__tank - distance * self.__fuel_consumption

    def check_fuel(self, distance: float) -> bool:
        return distance * self.__fuel_consumption <= self.__tank

    @property
    def tank(self):
        return self.__tank


class ElectricCar(GroundTransport, Transport, RadioMixIn):
    __battery_consumption: int = 210  # Ватт-час на км.

    def __init__(self, model, power):
        super().__init__(model)
        self.__battery = power * self.__battery_consumption

    def drive(self, distance: float):
        if not self._status_engine:
            print("Двигатель не заведен")
        elif not self.check_battery(distance):
            print("Не хватает топлива в баке")
        else:
            print("Поездка прошла успешно")
            self._mileage = self._mileage + distance
            self.__battery = self.__battery - distance * self.__battery_consumption

    def check_battery(self, distance: float) -> bool:
        return distance * self.__battery_consumption <= self.__battery

    @property
    def battery(self):
        return self.__battery
