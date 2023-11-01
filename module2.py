from abc import ABC, abstractmethod


class GroundTransport(ABC):
    """ Наземный транспорт """

    @abstractmethod
    def drive(self):
        ...


class PassengerTransport(GroundTransport):

    def __init__(self, passengers: int):
        self.__passengers = passengers

    def drive(self):
        print("Движется пассажирский транспорт")

    def __str__(self):
        return f"Пассажиры: {self.__passengers} \n"


class ElectricTransport(GroundTransport):

    def __init__(self, battery: int):
        self.__battery = battery

    def drive(self):
        print("Движется  электро-транспорт")

    def __str__(self):
        return f"Заряд: {self.__battery} \n"


class ElectricBus(ElectricTransport, PassengerTransport):

    def __init__(self, passengers: int, battery: int):
        ElectricTransport.__init__(self, battery)
        PassengerTransport.__init__(self, passengers)

    def __str__(self):
        return ElectricTransport.__str__(self) + \
               PassengerTransport.__str__(self)


bus = ElectricBus(10, 500)
bus.drive()
print(bus)

print(ElectricBus.__mro__)
